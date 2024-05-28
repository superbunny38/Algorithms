class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        start_idx, end_idx = 0,1
        max_length = 0
        while start_idx <= end_idx and end_idx <= len(s):
            substring = s[start_idx:end_idx]
            if len(substring) == len(set(substring)):
                max_length = max(len(set(substring)),max_length)
                end_idx +=1
            else:
                start_idx +=1
                end_idx +=1
        return max_length
