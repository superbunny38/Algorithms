class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        megazine_storage = Counter(list(magazine))

        for note in ransomNote:
            if note in megazine_storage:
                megazine_storage[note] -=1
                if megazine_storage[note] == 0:
                    del megazine_storage[note]
            else:
                return False
        return True

s = Solution().canConstruct(ransomNote = "a", magazine = "b")
print(s)
s = Solution().canConstruct(ransomNote = "aa", magazine = "aab")
print(s)