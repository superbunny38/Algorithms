#include <iostream>
#include <string>
#include <utility> // Required for std::forward

using namespace std;

class Widget {
public:
    // Case 1: Constructor takes an Lvalue (Copy)
    Widget(string& s) { cout << "Widget constructed via COPY (Lvalue)" << endl; }
    
    // Case 2: Constructor takes an Rvalue (Move)
    Widget(string&& s) { cout << "Widget constructed via MOVE (Rvalue)" << endl; }
};

// YOUR TASK: Fix this wrapper function!
// Currently, it takes T... args, but it doesn't forward them correctly.
template<typename T, typename... Args>
T createAndLog(Args&&... args) {
    cout << "Creating object..." << endl;
    return T(forward<Args>(args)...); // <--- This is wrong! It turns everything into Lvalues.
}

int main() {
    string name = "Alice";

    // Test 1: Passing an Lvalue
    // Should print "Widget constructed via COPY"
    createAndLog<Widget>(name);

    // Test 2: Passing an Rvalue
    // Should print "Widget constructed via MOVE"
    createAndLog<Widget>("Bob"); 
    
    return 0;
}