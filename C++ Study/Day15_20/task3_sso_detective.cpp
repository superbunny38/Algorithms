/*
You know that new is slow. The C++ Standard Library authors know this too. That is why std::string has a secret weapon: SSO (Small String Optimization).

Instead of always going to the Heap, std::string checks the length of the text:

Short String: Stored directly inside the object (Stack). Fast. ⚡

Long String: Allocated on the Heap. Slow. 🐢
*/

#include <iostream>
#include <new>     
#include <cstdlib> 
using namespace std;

void* operator new(size_t size) noexcept(false){
    cout<< "Global operator new called, size:"<<size<<" bytes"<<endl;
    void* ptr = malloc(size);

    if (!ptr){
        // If allocation fails, throw std::bad_alloc as per C++ standard
        throw bad_alloc{};  
    }
    return ptr;
}

void operator delete(void* ptr) noexcept{
    cout << "Global operator delete called" << endl;
    free(ptr);
}

int main(){

    for (int i =1;i<36;i++){
        string repeated_string(i,'A');
        cout << "String length "<<i<<": "<<repeated_string<<endl;

    }
    return 0;
}