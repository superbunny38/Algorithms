
class Solution {
public:
    int firstUniqChar(string s) {
        
        int count[26] = {0};
        int len = s.length();

        for (int i = 0; i<len;i++){
            count[s[i]-'a']++;
        }

        for (int k = 0;k<len;k++){
            if (count[s[k]-'a'] == 1){
                return k;
            }
        }

        return -1;
    }
};