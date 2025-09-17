class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        for s_word in s:
            s_dict[s_word] +=1
        
        for t_word in t:
            if t_word not in s_dict:
                return False
            s_dict[t_word] -= 1
            if s_dict[t_word] == 0:
                del s_dict[t_word]
        
        # print("remaining:",s_dict)
        if s_dict  == {}:
            return True
        return False
                        
s = Solution().isAnagram( s = "anagram", t = "nagaram")
print(s)