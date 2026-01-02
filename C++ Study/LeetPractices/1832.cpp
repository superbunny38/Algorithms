class Solution {
public:
    bool checkIfPangram(string sentence) {
        
        int count[26] = {0};
        int n_unique = 0;
        for (int i = 0; i<sentence.length();i++){
            if (count[sentence[i]-'a'] == 0){
                n_unique++;
                count[sentence[i]-'a']++;
            }
            if (n_unique == 26){
                return true;
            }
        }
        return false;
    }
};