#include <iostream>
using namespace std;

//cd Practice1
//g++ Practice1.cpp -o my_program
//./my_program

double findMedian_Conditional(double a, double b, double c) {
    // The median is the number that is NOT the minimum AND NOT the maximum.
    // It's the one in the middle.

    if ((b < a && a < c) || (c < a && a < b)) {
        // 'a' is in the middle (e.g., b < a < c or c < a < b)
        return a;
    } else if ((a < b && b < c) || (c < b && b < a)) {
        // 'b' is in the middle
        return b;
    } else {
        // 'c' must be in the middle (or all are equal, which is also c)
        return c;
    }
}

int main(){
    const double c1 {4e10};

    cout<<c1<<endl;

    //median
    cout << "Enter three numbers (x y z): ";
    double x,y,z;
    cin >> x >> y >> z;

    double median = findMedian_Conditional(x,y,z);

    cout << "The numbers are: " << x << ", " << y << ", " << z << endl;
    cout << "The median is: " << median << endl;

    return 0;
}