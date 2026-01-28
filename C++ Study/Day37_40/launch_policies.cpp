#include <iostream>
#include <future>
#include <chrono>
#include <thread>

using namespace std;

int main(){
    cout << "Main thread starting...\n";
    cout << "Main thread id: " << this_thread::get_id() << "\n";

    auto lazyFuture = async(launch::deferred, []{
        cout << "Lazy task started...\n";
        this_thread::sleep_for(chrono::milliseconds(500));
        cout << "Lazy thread id: " << this_thread::get_id() << "\n";
        cout << "Lazy task completed.\n";
    });

    auto asyncFuture = async(launch::async, []{
        cout << "Async task started...\n";
        this_thread::sleep_for(chrono::milliseconds(500));
        cout << "Async thread id: " << this_thread::get_id() << "\n";
        cout << "Async task completed.\n";
    });

    cout << "--- Main is doing other work ---\n";
    this_thread::sleep_for(chrono::milliseconds(100));
    cout << "--- Main calling .get() now ---\n\n";

    asyncFuture.get();
    lazyFuture.get(); // This will trigger the execution of the deferred task
    
    cout << "Main thread doing finishing...\n";

    return 0;
}