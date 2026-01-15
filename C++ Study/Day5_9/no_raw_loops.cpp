#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> data = {1, 5, 8, 9, 12, 4};

    // The syntax: [captures](parameters){ body }
    auto it = std::find_if(data.begin(), data.end(), [](int n) {

        return (n>10) && (n%2 == 0);
        
    });

    if (it != data.end()) {
        std::cout << "Found: " << *it << std::endl;
    } else {
        std::cout << "Not found" << std::endl;
    }
    return 0;
}