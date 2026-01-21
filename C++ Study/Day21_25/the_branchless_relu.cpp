/*
Branching: if (x > y) return x; else return y; (Requires a guess).
Branchless: result = x * (x > y) + y * (y >= x); (The CPU just does the math for both sides without ever having to "guess" a path).
*/

int relu_naive(int x){
    if (x<0){
        return 0;
    }
    else {
        return x;
    }
}

int relu_branchless_not_optimal(int x){
    return (x>=0)*1.0;
}

int relu_branchless(int x){
    return x & ~((x>>31));
}//Bitwise maskign is 1-cycle operation (i.e., physically the simplest thing a processor can do)