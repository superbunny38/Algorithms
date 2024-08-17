class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        real_n = 0
        for idx,digit in enumerate(digits):
            mul_by = 10**(len(digits)-idx-1)
            real_n += digit*mul_by
        str_list = list(str(real_n+1))
        return [int(x) for x in str_list]
