class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        while True:
            if num**2>x:
                break
            num += 1
        return num-1
