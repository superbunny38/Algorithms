#include <future>
#include <string>
#include <vector>
#include <iostream>
#include <chrono>
#include <thread>

using namespace std;

string ServiceA(){
    this_thread::sleep_for(chrono::milliseconds(200));
    cout << "Service A completed\n";
    return "Data from Service A";
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

int main(){
    auto start = chrono::high_resolution_clock::now();
    future<string> futureA = async(ServiceA);
    
    future<vector<int>> futureB = async(ServiceB);
    future<double> futureC = async(ServiceC);

    future_status statusC = futureC.wait_for(chrono::milliseconds(100));

    if (statusC == future_status::timeout){
        cout << "Service C is taking too long, proceeding without it.\n";
        cout << "cur elapsed:"
             << chrono::duration_cast<chrono::milliseconds>(
                    chrono::high_resolution_clock::now() - start).count() 
             << " ms\n";
    }


    //sleep 100 ms
    cout << "Reading available data...\n";
    this_thread::sleep_for(chrono::milliseconds(100));

    auto end = chrono::high_resolution_clock::now();
    cout << "Total elapsed time: " 
         << chrono::duration_cast<chrono::milliseconds>(end - start).count() 
         << " ms\n";

    return 0;

    // <--- INVISIBLE COMPILER GENERATED CODE --->
    //The destructor must block until the shared state is ready.
    // futureC.~future() calls futureC.wait();  <-- BLOCKS HERE for 2800ms more!
    // futureB.~future() ...
    // futureA.~future() ...

}//You believe your code finished in ~100ms because you called wait_for(100ms). In reality, your code took 3,000ms to exit.

/*
Even though you wanted to "timeout" and reply to the user immediately, the C++ runtime forced your thread to hang until the slow service finished anyway. You didn't save any latency.
*/