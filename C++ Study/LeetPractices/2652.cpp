class Solution {
public:
    long calcSum(int n, int k) {
            long m = n / k;
            return k * (m * (m + 1) / 2);
        }
    int sumOfMultiples(int n) {
        return calcSum(n, 3) + calcSum(n, 5) + calcSum(n, 7)
             - calcSum(n, 3 * 5) - calcSum(n, 3 * 7) - calcSum(n, 5 * 7)
             + calcSum(n, 3 * 5 * 7);
    }
};