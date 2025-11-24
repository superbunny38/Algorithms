#include <iostream>
using namespace std;

int q1(){
    int x;
    int ret = 0;
    cout << "Number:";
    cin >> x;
    for (int num = 3; num<=x;num++){
        if (num%3 == 0 || num % 5 == 0){
            ret += num;
        }
    }
    return ret;
}

unsigned int gcd(unsigned int const a, unsigned int const b){
    return b==0? a:gcd(b,a%b);
}

unsigned int gcd2(unsigned int a, unsigned int b){
    while (b != 0)
    {
        unsigned int r = a%b;
        a=b;
        b=r;
    }
    return a;
}

unsigned int lcm(){

}



void q2(unsigned int a, unsigned int b){
    //Greatest Common Divisor
    cout << "w recursion:"<< gcd(a,b);
    cout << "\nw/o recursion:"<<gcd2(a,b);
}

int main(){
    int ans1;
    ans1 = q1();
    cout << "1. Answer:"<<ans1;
    cout << "\n\n2. Answer:";
    q2(10,5);
    return 0;
}