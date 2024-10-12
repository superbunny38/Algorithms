class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = [0]*len(nums)
        max_sum[0] = nums[0]
        for i in range(1,len(nums)):
            max_sum[i] = max(nums[i],max_sum[i-1]+nums[i])
        # print(max_sum)
        return max(max_sum)
