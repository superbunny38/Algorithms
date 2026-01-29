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
class LockFreeStack{
    private:
        atomic<Node<T>*> head;
    
    public:
        LockFreeStack(): head(nullptr) {}

        void push(const T& data){
            Node<T>* newNode = new Node<T>(data);

            //Todo: Implement the CAS Loop here
            //1. Load the current head into a local variable 'expected_head
            Node<T>* expected_head = head.load();

            //2. Set the newNode's next pointer to expected_head
            newNode->next = expected_head;

            //3. while (!head.compare_exchange_weak(expected_head, newNode)){
                //if failed, expected_head is automatically updated to the REAL head
                //So just fix pointer: new_node->next = expected_head;
            //}

            while (!head.compare_exchange_weak(expected_head, newNode))
            {
                newNode->next = expected_head;
            }
            
        }

        void print_all(){
            Node<T>* current = head.load();
            int count = 0;
            while (current){
                count++;
                Node<T>*temp = current;
                current = current->next;
                delete temp;
            }
            cout << "Stack contained " << count << " items."<<endl;
        }

};

void test_lock_free(){
    LockFreeStack<int> stack;
    vector<thread> threads;

    //10 threads, each pushing 1000 items
    for (int i = 0;i<10;++i){
        threads.emplace_back([&stack](){
            for (int j = 0;j<1000;++j){
                stack.push(j);
            }
        });
    }

    for (auto& t:threads) t.join();

    stack.print_all();
}

int main(){
    test_lock_free();
    return 0;
}