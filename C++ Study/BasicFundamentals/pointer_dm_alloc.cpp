/*
다음 요구사항을 만족하는 프로그램을 작성하라.

- 정수 N을 입력 받아 N개의 정수를 저장할 배열을 만들 것.
- 입력: 5 1 2 3 4 5 출력: 1 2 3 4 5
- new/delete version과 malloc/free version 두 번 작성할 것
*/
#include <iostream>
#include <cstdlib> // malloc, free를 사용하기 위해 필요

using namespace std;

int main() {
    int N;
    
    // 1. N 입력 받기
    cout << "N을 입력하세요: ";
    cin >> N;

    // new & delete

    int* arr = new int[N];
    for (int i = 0;i<N;i++){
        cin >> arr[i];
    }

    for (int i = 0;i<N;i++){
        cout << arr[i] << " ";
    }

    cout << endl;

    delete[] arr;//배열이므로 []를 꼭 붙여야함


    //malloc & free

    int N2;

    cin >> N2;

    int* arr = (int*)malloc(sizeof(int)*N);

    for (int i = 0;i<N;i++){
        cin >> arr[i];
    }

    for (int i = 0;i<N;i++){
        cout << arr[i] << " ";
    }
    cout << endl;

    free(arr);

    return 0;
}