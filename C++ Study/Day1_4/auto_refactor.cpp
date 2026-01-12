// OLD C++

/*
std::map<std::string, int> scores;
scores.insert(std::make_pair("Alice", 10));
scores.insert(std::make_pair("Bob", 20));

for (std::map<std::string, int>::iterator it = scores.begin(); it != scores.end(); ++it) {
    std::string name = it->first;
    int score = it->second;
    // ... logic
}
*/
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    // TASK PART 1: Uniform Initialization ({})
    // Instead of using .insert() repeatedly, initialize the map directly.
    map<string, int> scores = {
        { "Alice", 10 }, 
        { "Bob", 20}   // <--- Add Bob here using the same syntax
    };

    // TASK PART 2: Range-based for loop + Structured Binding
    // Syntax Hint: for (auto [var1, var2] : container)
    for (const auto& [name, score] : scores) {
        
        // logic (e.g., printing them out to verify)
        // You can now use the variable names you defined in the [ ] above directly.
        cout << "Name: " << name << ", Score: " << score << endl;
    }

    // Check if "Charlie" exists in the map

    //Old C++
    // auto it = scores.find("Charlie"); 

    // if (it != scores.end()) {
    //     cout << "Found Charlie! Score: " << it->second << endl;
    // } else {
    //     cout << "Charlie not found." << endl;
    // }

    // PROBLEM: The variable 'it' is still accessible here! 
    // If I search for someone else later, I might accidentally mix up my iterators.

    if (auto it = scores.find("Charlie");it != scores.end()){
        cout << "Found Charlie! Score: "<<it->second << endl;
    } else{
        cout << "Charlie not found."<<endl;
    }

    return 0;
}