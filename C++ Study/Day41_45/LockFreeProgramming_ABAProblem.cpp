#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

template<typename T>
struct Node{
    T data;
    Node* next;
    Node(const T& value) : data(value), next(nullptr) {}
};

template<typename T>
struct alignas(16) TaggedPointer
{
    Node<T>* ptr;
    uintptr_t counter;
};


template<typename T>
class LockFreeStack{
    private:
        atomic<TaggedPointer<T>> head;
    
    public:
        LockFreeStack() {
            TaggedPointer<T> dummy = {nullptr, 0};
            head.store(dummy);
        }

        //push
        void push(const T& data){
            Node<T>* newNode = new Node<T>(data);

            //Todo: Implement the CAS Loop here
            //1. Load the current head into a local variable 'expected_head
            TaggedPointer<T> expected_head = head.load(memory_order_relaxed);

            while ( true )
            {
                newNode->next = expected_head.ptr;

                TaggedPointer<T> new_head = {newNode, expected_head.counter + 1};
                if (head.compare_exchange_weak(expected_head, new_head, memory_order_release, memory_order_relaxed))
                    break;
            }
            
        }

        //pop
        bool pop(T& result){

            TaggedPointer<T> expected_head = head.load(memory_order_acquire);

            while (true){
                if (expected_head.ptr == nullptr){
                    return false; //stack empty
                }
                Node<T>* next_node = expected_head.ptr->next;

                TaggedPointer<T> new_head = {next_node, expected_head.counter + 1};

                if (head.compare_exchange_weak(expected_head, new_head, memory_order_acquire, memory_order_acquire)){
                    result = expected_head.ptr->data;
                    // delete expected_head.ptr;
                    return true;
                }
            }
            
        }

        bool is_lock_free(){
            return head.is_lock_free();
        }

};

void test_lock_free() {
    LockFreeStack<int> stack;
    
    // Verify we are actually using hardware atomics
    if (stack.is_lock_free()) {
        cout << "System supports 128-bit hardware atomics! (Lock-Free)" << endl;
    } else {
        cout << "Warning: System using software locks (Not truly Lock-Free)" << endl;
    }

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
