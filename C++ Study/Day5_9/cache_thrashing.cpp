#include <chrono>
#include <iostream>


int matrix[10000][10000];

int main(){

    
    auto start = std::chrono::high_resolution_clock::now();

    for (int i=0;i<10000;i++){
        for (int j=0;j<10000;j++){
            matrix[i][j] += 1;
        }
    }


    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> duration = end - start;


    std::cout << "[Fast Loop] Time taken: " << duration.count() << " ms" << std::endl;

    start = std::chrono::high_resolution_clock::now();

    for (int i=0;i<10000;i++){
        for (int j=0;j<10000;j++){
            matrix[j][i] += 1;
        }
    }


    end = std::chrono::high_resolution_clock::now();

    duration = end - start;


    std::cout << "[Slow Loop] Time taken: " << duration.count() << " ms" << std::endl;

    return 0;
}