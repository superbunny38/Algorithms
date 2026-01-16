//Reference counting

/*
- Unique: std::unique_ptr<FILE, decltype(&fclose)> (Hardcoded type)
- Shared: std::shared_ptr<FILE> (Type Erasure—it just works!)
*/
#include <memory>
#include <cstdio>
#include <iostream> 

using namespace std;

int main(){
    auto file_name = "abc.txt";
    shared_ptr<FILE> ptr1(fopen(file_name, "r"), &fclose);
    cout << ptr1.use_count() << endl;
    {
        auto ptr2 = ptr1;
        cout << ptr2.use_count() << endl;
    }

    cout << ptr1.use_count() << endl;

    return 0;
}