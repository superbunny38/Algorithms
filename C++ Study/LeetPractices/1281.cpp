class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1;
        int summation = 0;

        while (n>0){
            int number = n%10;
            product *= number;
            summation += number;
            n/=10;
        }
        return product - summation;
    }
};