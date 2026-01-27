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
};