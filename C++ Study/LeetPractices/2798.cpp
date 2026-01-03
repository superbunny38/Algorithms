class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int ret = 0;
        for (const auto&hour : hours){
            if (hour>=target){
                ret++;
            }
        }

        return ret;

    }
};