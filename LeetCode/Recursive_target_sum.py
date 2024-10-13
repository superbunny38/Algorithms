class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        value = nums[0]
        if len(nums) == 1:
            if value*1 == target and value*(-1) == target:
                return 2
            elif value*(-1) == target:
                return 1
            elif value*1 == target:
                return 1
            else:
                return 0
        else:
            return self.findTargetSumWays(nums[1:],target-value)+self.findTargetSumWays(nums[1:],target+value)
        
