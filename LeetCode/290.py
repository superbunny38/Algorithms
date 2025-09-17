class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        pattern_to_s, s_to_pattern = dict(),dict()
        
        for idx in range(len(pattern)):
            p_char, s_word = pattern[idx], s[idx]
            
            if p_char in pattern_to_s:
                if s_word != pattern_to_s[p_char]:
                    return False
            else:
                pattern_to_s[p_char] = s_word
            
            if s_word in s_to_pattern:
                if p_char != s_to_pattern[s_word]:
                    return False
            else:
                s_to_pattern[s_word] = p_char
            # print("s_to_pattern:",s_to_pattern)
            # print("pattern_to_s:",pattern_to_s)
        return True

s = Solution().wordPattern(pattern = "abba", s = "dog cat cat dog")
print(s)