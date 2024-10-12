import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memoization = [math.inf for _ in range(amount+1)]
        memoization[0] = 0
        # coins = sorted(coins)
        min_c = min(coins)

        for num in range(amount+1):
            for c in coins:
                if num-c>=0:
                    memoization[num] = min(1+memoization[num-c],memoization[num])

        if memoization[-1]>amount:
            return -1
        else:
            return memoization[-1]
