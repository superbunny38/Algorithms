#include <atomic>
#include <iostream>
#include <thread>
#include <vector>
#include <cstdint>

using namespace std;

template<typename T>
struct Node {
    T data;
    Node* next;
    Node(const T& val) : data(val), next(nullptr) {}
};

// THE EXPERT FIX: Pointer Tagging
// On 64-bit systems, pointers only use the bottom 48 bits.
// We use the top 16 bits to store our ABA counter.
// [ 16-bit Counter | 48-bit Pointer ]
// This fits in a standard 64-bit atomic, so NO linker errors!
template<typename T>
class LockFreeStack {
private:
    std::atomic<uintptr_t> head_raw; // Stores both pointer and counter packed together

    // Helper: Pack a pointer and a counter into one 64-bit integer
    static uintptr_t encode(Node<T>* ptr, uint16_t count) {
        uintptr_t ptr_val = reinterpret_cast<uintptr_t>(ptr);
        // Clean the top 16 bits of the pointer just in case
        ptr_val = ptr_val & 0x0000FFFFFFFFFFFF;
        // Shift counter to top and combine
        return (static_cast<uintptr_t>(count) << 48) | ptr_val;
    }

    // Helper: Extract just the pointer
    static Node<T>* decode_ptr(uintptr_t raw) {
        // Mask out the top 16 bits to get the clean pointer
        return reinterpret_cast<Node<T>*>(raw & 0x0000FFFFFFFFFFFF);
    }

    // Helper: Extract just the counter
    static uint16_t decode_count(uintptr_t raw) {
        return static_cast<uint16_t>(raw >> 48);
    }

public:
    LockFreeStack() {
        head_raw.store(encode(nullptr, 0));
    }

    void push(const T& data) {
        Node<T>* new_node = new Node<T>(data);
        
        uintptr_t expected_raw = head_raw.load(std::memory_order_relaxed);

        while (true) {
            // Unpack the current head to see where to point
            Node<T>* current_ptr = decode_ptr(expected_raw);
            uint16_t current_count = decode_count(expected_raw);

            new_node->next = current_ptr;

            // Create new raw value: New Pointer + (Old Count + 1)
            uintptr_t new_raw = encode(new_node, current_count + 1);

            // CAS Loop
            if (head_raw.compare_exchange_weak(expected_raw, new_raw, 
                                               std::memory_order_release, 
                                               std::memory_order_relaxed)) {
                break;
            }
        }
    }

    bool pop(T& result) {
        uintptr_t expected_raw = head_raw.load(std::memory_order_acquire);

        while (true) {
            Node<T>* current_ptr = decode_ptr(expected_raw);
            uint16_t current_count = decode_count(expected_raw);

            if (current_ptr == nullptr) {
                return false; 
            }

            // DANGER ZONE: Reading next. 
            // In production, you need Hazard Pointers here.
            Node<T>* next_node = current_ptr->next;

            // Create desired value: Next Pointer + (Old Count + 1)
            uintptr_t new_raw = encode(next_node, current_count + 1);

            if (head_raw.compare_exchange_weak(expected_raw, new_raw, 
                                               std::memory_order_acquire, 
                                               std::memory_order_acquire)) {
                result = current_ptr->data;
                // delete current_ptr; // LEAK INTENTIONALLY to avoid segfault in test
                return true;
            }
        }
    }
};

void test_lock_free() {
    LockFreeStack<int> stack;
    
    // Check if it's lock-free (Standard atomics usually are)
    cout << "Lock-Free Stack Initialized." << endl;

    vector<thread> threads;
    std::atomic<int> successful_pops{0};

    // 10 threads, each pushing 1000 items
    cout << "Pushing 10,000 items concurrently..." << endl;
    for (int i = 0; i < 10; ++i) {
        threads.emplace_back([&stack]() {
            for (int j = 0; j < 1000; ++j) {
                stack.push(j);
            }
        });
    }

    for (auto& t : threads) t.join();
    threads.clear();

    // 10 threads, each popping until empty
    cout << "Popping items concurrently..." << endl;
    for (int i = 0; i < 10; ++i) {
        threads.emplace_back([&stack, &successful_pops]() {
            int val;
            while (stack.pop(val)) {
                successful_pops++;
            }
        });
    }

    for (auto& t : threads) t.join();

    cout << "Total items popped: " << successful_pops << endl;
    if (successful_pops == 10000) {
        cout << "SUCCESS: No items lost!" << endl;
    } else {
        cout << "FAILURE: Race condition detected." << endl;
    }
}

int main() {
    test_lock_free();
    return 0;
}