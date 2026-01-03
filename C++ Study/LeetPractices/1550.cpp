class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int n_consec = 0;
        int vector_length = arr.size();

        for (int i = 0; i<vector_length;i++){
            if (arr[i]%2 == 0){
                n_consec = 0;
            }
            else{
                n_consec++;
            }

            if (n_consec == 3){
                return true;
            }
        }
        return false;
    }
};