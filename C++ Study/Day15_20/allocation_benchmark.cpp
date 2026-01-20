// The Goal: Measure the time difference between Stack allocation and Heap allocation.

#include <iostream>
#include <chrono>
#include <vector>

using namespace std;

int main(){

    const int ITERATIONS = 1000000;
    volatile int sink = 0;//volatile prevents the compiler from optimizing the loop away

    cout << "Benchmarking " << ITERATIONS << " iterations...\n";
    
    // -- CASE A: STACK ALLOCATION

    auto start_stack = chrono::high_resolution_clock::now();

    for (int i = 0;i<ITERATIONS;++i){
        int x = i;
    }

    auto end_stack = chrono::high_resolution_clock::now();

    // -- CASE B: HELP ALLOCATION
    auto start_heap = chrono::high_resolution_clock::now();

    for (int i = 0;i<ITERATIONS;++i){
        int* heapIntPtr = new int(i);
        delete heapIntPtr;
        heapIntPtr = nullptr;
    }

    auto end_heap = chrono::high_resolution_clock::now();

    auto stack_time = chrono::duration_cast<chrono::microseconds>(end_stack-start_stack).count();
    auto heap_time = chrono::duration_cast<chrono::microseconds>(end_heap-start_heap).count();

    if (stack_time>0){
        cout << "Heap is " << (double)heap_time/stack_time << "x times slower than Stack.\n";
    }

    return 0;
}