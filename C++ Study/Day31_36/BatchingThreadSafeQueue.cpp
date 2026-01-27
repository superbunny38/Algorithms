#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>
#include <chrono>  

using namespace std;
template <typename T>

class ThreadSafeQueue {
    private:
        queue<T> q;
        mutable mutex mtx;
        condition_variable cv;
        bool shutdown_flag = false;
    
    public:
        void push(T value){
            {lock_guard<mutex> lock(mtx);
            q.push(move(value));}
            cv.notify_one();
        }

        bool pop(T& result){
            unique_lock<mutex> lock(mtx);//locking
            cv.wait(lock, [this]{ return (!q.empty() || shutdown_flag); });
            if (shutdown_flag && q.empty()) {
                return false; // Indicate that the queue is shutting down
            }
            result = move(q.front());
            q.pop();
            return true;
        }
        void shutdown() {
            {lock_guard<mutex> lock(mtx);
            shutdown_flag = true;}
            cv.notify_all();
        }
        
        void push_batch(vector<T> values){
            {
                lock_guard<mutex> lock(mtx);
                for (auto& value : values) {
                    q.push(move(value));
                }
            }
            cv.notify_all();
        }
};



/*
The "Aftermath" Cost 📉
Think of it like this:

notify_one(): You tap one person on the shoulder.

OS Work: 1 context switch (wake up thread), 1 lock acquisition.

Cost: Low.

notify_all(): You pull the fire alarm. 🚨

OS Work: 5 (or 500) context switches, 5 threads fighting for the same lock.

Cost: Very High (The "Thundering Herd").
*/