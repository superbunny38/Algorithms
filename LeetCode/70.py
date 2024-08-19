class Solution:
    def climbStairs(self, n: int) -> int:
        memoization = [0,1,2]
        if n <= 2:
            return memoization[n]
        for _ in range(n-2):
            new = memoization[-1]+memoization[-2]
            memoization.append(new)
        return memoization[n]
