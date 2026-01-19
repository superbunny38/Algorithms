/*
Task 2: The Unique Ownership Transfer
Now, let's see how this works with the standard library tools. Since std::unique_ptr has those = delete lines built-in, you cannot pass it to a function by value (copying it). You must move it.

Your Mission: Write a program that passes a unique_ptr into a function.
*/

#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <memory>
#include <utility>

using namespace std;

class MyResource {
    public:
    MyResource(){cout<<"Resource Acquired!"<<endl;}
    ~MyResource(){cout<<"Resource Released!"<<endl;}
};

void passTheParcel(unique_ptr<MyResource> ptr){

    cout<<"I have the resource!"<<endl;

}

int main(){
    auto ptr = make_unique<MyResource>();
    passTheParcel(move(ptr));
    return 0;
}

/*

To check your intuition: After you call passTheParcel(std::move(ptr)), if you tried to use ptr again inside main (e.g., ptr->doSomething()), what do you think would happen?

A. After std::move(ptr), the source ptr becomes nullptr.

*/