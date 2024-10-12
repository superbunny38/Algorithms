class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for explore_idx in range(1,len(prices)):
            buy = min(buy, prices[explore_idx])
            res = max(res, prices[explore_idx]-buy)

        return res
        
