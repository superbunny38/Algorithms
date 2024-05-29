class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            num = -int(x[::-1])
        else:
            num = int(x[::-1])
        if num> 2**31-1 or num < -2**31:
            return 0
        return num
