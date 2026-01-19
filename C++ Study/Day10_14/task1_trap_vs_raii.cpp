#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <memory>

using namespace std;

class MyResource {
    public:
    MyResource(){cout<<"Resource Acquired!"<<endl;}
    ~MyResource(){cout<<"Resource Released!"<<endl;}
};

void testLeak(){
    // auto raw_ptr = new MyResource;
    // throw 1;
    // delete raw_ptr;

    auto unique_ptr = make_unique<MyResource>();
    throw 1;

}


int main() {
    try {
        testLeak();
    } catch (int e) {
        cout << "Caught exception: " << e << endl;
    }
    return 0;
}