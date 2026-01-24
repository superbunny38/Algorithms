#include <iostream>
#include <thread>

using namespace std;

int number = 0;

void inc(){
    for(int i = 0; i < 100000; i++){
        number++;
    }
}

int main(){
    thread t1(inc);
    thread t2(inc);

    t1.join();
    t2.join();

    cout << "Final number: " << number << endl;
    return 0;
}

