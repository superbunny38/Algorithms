class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        # print("cost:",cost)
        n,minCost = len(cost),0

        if n<3:
            return sum(cost)
        
        for idx in range(0,n-1,3):
            # print("idx:",idx)
            tmpCost = cost[idx]+cost[idx+1]
            minCost += tmpCost
        if n%3 == 1:
            minCost += cost[-1]
        return minCost 
