#include <iostream>
#include <vector>
#include <string>
#include <chrono> // Required for timing

using namespace std;

// 1. Function that takes by VALUE (Forces a Deep Copy)
void processCopy(vector<string> v) {
    // We don't need to do anything here. 
    // Just receiving the copy is enough to trigger the heavy work.
}

// 2. Function that takes by RVALUE REFERENCE (Allows Moving)
void processMove(vector<string>&& v) {
    // This receives the original vector's guts (pointers).
    // No copying of data happens here.
    vector<string> stolenData(move(v));
}

int main() {
    // SETUP: Create a huge vector
    // Hint: Use the constructor (size, value)
    vector<string> bigVec(1000000, "test");
    
    cout << "Vector created with 1,000,000 strings." << endl;

    // ==========================================
    // TEST 1: COPY
    // ==========================================
    auto startCopy = chrono::high_resolution_clock::now();
    
    // Call the function that takes by value
    processCopy(bigVec); 

    auto endCopy = chrono::high_resolution_clock::now();
    auto copyTime = chrono::duration_cast<chrono::milliseconds>(endCopy - startCopy);
    cout << "Copy took: " << copyTime.count() << "ms" << endl;

    // ==========================================
    // TEST 2: MOVE
    // ==========================================
    auto startMove = chrono::high_resolution_clock::now();

    // Call the function that takes by Rvalue Ref
    // CRITICAL: You must cast bigVec to an rvalue using std::move()
    processMove(std::move(bigVec)); 

    auto endMove = chrono::high_resolution_clock::now();
    auto moveTime = chrono::duration_cast<chrono::milliseconds>(endMove - startMove);
    cout << "Move took: " << moveTime.count() << "ms" << endl;

    // OPTIONAL: Check what happened to bigVec after the move
    cout << "Size of bigVec after move: " << bigVec.size() << endl;

    return 0;
}