#include <stdio.h>
#include <cstdio>

using namespace std;

class FileHandle {
    private:
    FILE* file_p;

    public:
    FileHandle(const char* filename){file_p = fopen(filename,"r");}
    ~FileHandle(){
        if (file_p != nullptr){
            fclose(file_p);
            file_p = nullptr;
        }
    }

    // Delete Copying
    // This stops the "Double Free" crash by forbidding copies.

    FileHandle(const FileHandle&) = delete;
    FileHandle& operator = (const FileHandle&) = delete;

};