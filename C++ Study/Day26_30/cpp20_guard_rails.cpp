#include <concepts>

using namespace std;

template<typename T>
concept Number = (integral <T> || floating_point<T>) && !same_as<T, bool> && !same_as<T, char>;

auto multiply(Number auto a, Number auto b) {
    return a * b;
}


int main() {
    auto result1 = multiply(true, false);
    auto result = multiply(10, 20);
    return 0;
}