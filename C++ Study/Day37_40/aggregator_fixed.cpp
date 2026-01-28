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
    
    //Define the tasks
    packaged_task<string()> taskA(ServiceA);
    packaged_task<vector<int>()> taskB(ServiceB);
    packaged_task<double()> taskC(ServiceC);

    //Get the futures before starting the threads
    future<string> futureA = taskA.get_future();
    future<vector<int>> futureB = taskB.get_future();
    future<double> futureC = taskC.get_future();

    thread(move(taskA)).detach();
    thread(move(taskB)).detach();

    thread threadC(move(taskC));
    if (threadC.joinable()){
        threadC.detach(); // Detach the thread to allow it to run independently
    }

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
    
    string resA = futureA.get(); 
    cout << "Got A: " << resA << endl;

    vector<int> resB = futureB.get();
    cout << "Got B (size): " << resB.size() << endl;

    auto end = chrono::high_resolution_clock::now();
    cout << "Total elapsed time: " 
         << chrono::duration_cast<chrono::milliseconds>(end - start).count() 
         << " ms\n";

    return 0;
}