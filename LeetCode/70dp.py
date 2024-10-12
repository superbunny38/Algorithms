class Solution:
    def climbStairs(self, n: int) -> int:
        
        memoization = [0,1,2]

        while len(memoization)<=n:
            m = memoization[-1]+memoization[-2]
            memoization.append(m)

        print(memoization)

        return memoization[n]
