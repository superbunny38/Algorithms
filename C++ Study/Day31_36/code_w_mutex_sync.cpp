#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

int number = 0;

mutex mtx;

void inc(){
    mtx.lock();

    for(int i = 0; i < 100000; i++){
        number++;
    }

    mtx.unlock();
}

int main(){
    thread t1(inc);
    thread t2(inc);

    t1.join();
    t2.join();

    cout << "Final number: " << number << endl;
    return 0;
}
