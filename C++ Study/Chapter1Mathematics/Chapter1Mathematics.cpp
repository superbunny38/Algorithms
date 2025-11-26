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

//q3
unsigned int lcm(unsigned int a, unsigned int b){
    int h = gcd(a,b);
    return h ? (a*(b/h)):0;
}


void q2(unsigned int a, unsigned int b){
    //Greatest Common Divisor
    cout << "w recursion:"<< gcd(a,b);
    cout << "\nw/o recursion:"<<gcd2(a,b);
}

//q4
bool is_prime(int const num){
    if (num <= 3){
        return num >1;
    }

    else if (num %2 == 0 || num % 3 == 0){
        return false;
    }
    else{
        for (int i = 5; i*i<=num; i += 6){
            if (num%i == 0 || num% (i+2) == 0){
                return false;
            }
        }
        return true;
    }
}

int main(){
    int ans1;
    ans1 = q1();
    cout << "1. Answer:"<<ans1;
    cout << "\n\n2. Answer:";
    q2(10,5);
    cout << "\n3. Answer:" << lcm(10,5);
    return 0;
}