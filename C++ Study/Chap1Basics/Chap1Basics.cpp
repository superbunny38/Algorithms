#include <iostream>
#include <string> 
using namespace std;

void variables(){
    int i1 = 2;
    int i2, i3 = 5; // i2는 초기화되지 않음
    float pi = 3.14;
    double x = -1.5e-6;
    char c1 = 'a',c2 = 36;//char의 용도 두 가지: 1. 문자 2. 아주 짧은 정수
    bool cmp = i1<pi, happy = true;
    string name = "Herbert";
}

int main(){
    variables();
    return 0;
}