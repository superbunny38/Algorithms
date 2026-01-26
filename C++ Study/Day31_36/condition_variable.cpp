#include <condition_variable>
#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

condition_variable cv;
mutex mtx;

int value = 0;

void add(int number){
    unique_lock<mutex> lock(mtx);
    value += number;
    cout << "Added " << number << ", new value: " << value << endl;
    cv.notify_one();
}

void subtract(int number){
    unique_lock<mutex> ulock(m);
    cv.wait(ulock,[]{return (val!=0)? true : false;});

    if (value >= number) {
        value -= number;
        cout << "Subtracted " << number << ", new value: " << value << endl;
    } else {
        cout << "Not enough value to subtract " << number << endl;
    }
    cout << "Final value: " << value << endl;
}

int main(){
    thread t1(add, 50);
    thread t2(subtract, 30);

    t1.join();
    t2.join();

    return 0;
}