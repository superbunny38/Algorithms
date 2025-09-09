# import random
class Solution:
    def removeAnagrams(self, words):
        if not words:
            return []
        
        result = [words[0]]  
        
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i-1]):
                result.append(words[i])
            
        return result
                        
        
s = Solution()
a1 = s.removeAnagrams(words = ["abba","baba","bbaa","cd","cd"])
print(a1)
a2 = s.removeAnagrams(words = ["a","b","c","d","e"])
print(a2)