class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        break_list = s.split()[-1]
        # print("break list:",break_list)
        return len(break_list)
