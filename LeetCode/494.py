class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def findSum(idx,total):
            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            else:
                if (idx,total) in dp:
                    return dp[(idx,total)]
                else:
                    dp[(idx,total)] = findSum(idx+1,total+nums[idx])+findSum(idx+1,total-nums[idx])
                    return dp[(idx,total)]
        return findSum(0,0)
