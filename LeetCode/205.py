class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t, map_t_to_s = dict(),dict()
        
        for idx in range(len(s)):
            char_s, char_t = s[idx], t[idx]
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t
            
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
        return True
            
        
s = Solution().isIsomorphic(s = "egg", t = "add")
print(s)

s = Solution().isIsomorphic(s = "bbbaaaba", t = "aaabbbba")
print(s)