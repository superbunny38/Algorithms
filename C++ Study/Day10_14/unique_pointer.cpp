#include <cstdio>
#include <memory>
#include <cassert>


using namespace std;

// std::unique_ptr<ResourceType, DeleterType> variableName(value, deleterFunction);

int main(){
    auto file_name = "abc";
    unique_ptr<FILE, decltype(&fclose)> ptr1(fopen(file_name, "r"), &fclose);

    //move ownership from ptr1 to ptr2
    if (ptr1){
        auto ptr2 = move(ptr1);

        assert(ptr1.get() == nullptr);
        assert(ptr2.get() != nullptr);
    }

    return 0;
}

