#include <iostream>
#include <cmath>
#include <vector>
class Solution {
public:
    int differenceOfSum(std::vector<int>& nums) {
        int element_sum = 0, digit_sum = 0;
        for (auto& num:nums){
            element_sum += num;
            
            while (num>0){
                digit_sum+=num%10;
                num/=10;
            }
        }
        return std::abs(element_sum - digit_sum);
    }
};