#include <algorithm>

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        for (const auto& account: accounts){
            int current_wealth = 0;
            for (const auto& money: account){
                current_wealth += money;
            }

            maxWealth = max(maxWealth, current_wealth);
        }
        return maxWealth;
    }
};