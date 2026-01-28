#include <future>
#include <string>
#include <vector>
#include <iostream>
#include <chrono>
#include <thread>
#include <queue>
#include <functional>
#include <mutex>
#include <condition_variable>

using namespace std;

class ThreadPool{
    // component 1) A place to store the fixed number of running threads.
    // component 2) A place to store the pending tasks.
    // component 3) Synchronization tools to prevent the threads from fighting over the queue (race conditions)
    public:
        ThreadPool(size_t numThreads) : stop(false){// initializes a boolean member variable named stop to the value false when a new ThreadPool object is created.
            for(size_t i = 0;i<numThreads;++i){
                workers.emplace_back(
                    [this]{
                        while (true)
                        {
                            function<void()> task;
                            {//lock scope
                                unique_lock<mutex> lock(this->queueMutex);

                                //wait until the stop flag is true or the queue is not empty
                                this->condition.wait(lock,
                                    [this]{ return this->stop || !this->tasks.empty(); });
                                
                                //If stop flag is true and there are no tasks, exit the thread
                                if(this->stop && this->tasks.empty()){
                                    return;
                                }

                                //Get the next task from the queue
                                task = move(this->tasks.front());
                                this->tasks.pop();
                            }//lodk released here
                        //execute the task outside the lock wo that the other threads can grab other tasks parallely
                        task();
                        }
                       
                    }
                );
            }
        };
        ~ThreadPool(){
            {
                unique_lock<mutex> lock(queueMutex);
                stop = true;
            }
            condition.notify_all();
            for(thread &worker: workers){
                if(worker.joinable()){
                    worker.join();//the main thread pauses and waits for every worker thread to finish its current loop iteration and exit gracefully.
                }
            }
        };

        //F: function type
        template<class F>
        auto enqueue(F&& f) -> future<decltype(f())>{
            using return_type =decltype(f());// alias the return type of the functionn

            //create a packaged task on the heap using make_shared
            //In C++, if you create a variable inside a function, it is destroyed when the function ends.
            auto task = make_shared<packaged_task<return_type()>>(forward<F>(f));

            //get the future from the packaged task so that we can return it to the caller
            future<return_type> res = task->get_future();

            {//lock scope
                unique_lock<mutex> lock(queueMutex);

                //don't allow enqueueing after stopping the pool
                if(stop){
                    throw runtime_error("enqueue on stopped ThreadPool");
                }

                //add the task to the queue
                //we capture the task (the shared_ptr) by value to ensure it remains valid when executed by the worker thread
                //lambda: a function with no name
                //[campture list](parameters) { function body }
                tasks.emplace([task](){ (*task)(); });

                /*
                [task]: "Bring the task variable inside this box with me."

                (): "I don't need any new ingredients to run."

                { (*task)(); }: "When you run me, I will execute the task I brought with me."
                */

            }//lock releases here

            condition.notify_one(); //notify one thread that a new task is available
            return res;

        }
    
    private:
        vector<thread> workers;
        queue<function<void()>> tasks;

        mutex queueMutex;
        condition_variable condition;
        bool stop;

};

string ServiceA() {
    this_thread::sleep_for(chrono::milliseconds(200));
    throw runtime_error("CRITICAL: User Database Connection Failed!"); 
    return ""; // This line is never reached
}

vector<int> ServiceB(){
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << "Service B completed\n";
    return {1, 2, 3, 4, 5};
}

double ServiceC(){
    this_thread::sleep_for(chrono::milliseconds(3000));
    cout << "Service C completed\n";
    return 42.0;
}

//New Way
int main(){
    ThreadPool pool(4); // Create a thread pool with 4 workers
    auto start = chrono::high_resolution_clock::now();

    //Enqueue the tasks
    future<string> futureA = pool.enqueue(ServiceA);
    future<vector<int>> futureB = pool.enqueue(ServiceB);
    future<double> futureC = pool.enqueue(ServiceC);

    future_status statusC = futureC.wait_for(chrono::milliseconds(100));
    if (statusC == future_status::timeout){
        cout << "Service C is taking too long, proceeding without it.\n";
        cout << "cur elapsed:"
             << chrono::duration_cast<chrono::milliseconds>(
                    chrono::high_resolution_clock::now() - start).count() 
             << " ms\n";
    }
    else{
        double resultC = futureC.get();
        cout << "Service C result: " << resultC << "\n";
    }

    try{
        string resA = futureA.get(); 
        cout << "Got A: " << resA << endl;
    }
    catch(const exception& e){
        cerr << "Error retrieving result from Service A: " << e.what() << endl;
    }

    vector<int> resB = futureB.get();
    cout << "Got B (size): " << resB.size() << endl;

    auto end = chrono::high_resolution_clock::now();
    cout << "Total elapsed time: " 
         << chrono::duration_cast<chrono::milliseconds>(end - start).count() 
         << " ms\n";

    return 0;
}
