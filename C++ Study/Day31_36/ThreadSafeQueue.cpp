#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>
#include <chrono>  

using namespace std;

template<typename T>
class ThreadSafeQueue {
    private:
    queue<T> q;
    mutable mutex mtx;
    condition_variable cv;
    
    public:
    //[Push (The Producer)]
    void push(T value){
        lock_guard<mutex> lock(mtx);
        q.push(value,T);
        cv.notify_one();
    }

    //[Pop (The consumer)]
    void pop(T& result){
        unique_lock<mutex> ulock(mtx);
        cv.wait(ulock, []{return (q.size() != 0)? true: false;});
        result = move(q.front());
        q.pop();
        
    }

    bool empty() const{
        lock_guard<mutex> lock(mtx);
        return q.empty();
    }

};


// --- TEST HARNESS ---
// Simulates Service: 
// 5 Threads producing "Requests"
// 5 Threads "Serving" them.
void test_concurrency(){
    ThreadSafeQueue<int> ts_queue;
    vector<thread> producers;
    vector<thread> consumers;

    //Start producers
    for(int i = 0;i<5;i++){
        producers.emplace_back([&ts_queue, i](){
            for(int j=0;j<100;j++){
                int request = i*1000 + j;
                cout << "Producing request: " << request << endl;
                ts_queue.push(request);
                this_thread::sleep_for(chrono::milliseconds(1));
            }
        });
    }

    //Start consumers
    for(int i = 0;i<5;i++){
        consumers.emplace_back([&ts_queue, i](){
            for(int j=0;j<100;j++){
                int request;
                ts_queue.pop(request);
                cout << "Consumer " << i << " served request: " << request << endl;
                this_thread::sleep_for(chrono::milliseconds(2));
            }
        });
    }

    //Join all
    for(auto& prod : producers){
        prod.join();
    }

    for(auto& cons : consumers){
        cons.join();
    }

    cout << "All requests processed." << endl;
}

int main(){
    test_concurrency();
    return 0;
}