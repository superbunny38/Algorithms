/*
포인터를 사용하여 문자열의 내용을 모두 대문자로 바꾸는 함수
*/

#include <iostream>
using namespace std;

void strUpper(char* str){
    
    for (;*str;++str){
       *str = *str-32;
    }
}

int main(){
    char str[] = "hello my world";
    strUpper(str);
    cout<<str;
    return 0;
}