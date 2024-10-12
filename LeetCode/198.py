class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2 :
            return max(nums)
            
        rob_m = [0]*len(nums)
        rob_m[0] = nums[0]
        rob_m[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            rob_m[i] = max(rob_m[i-1],rob_m[i-2]+nums[i])
        print(rob_m)

        return rob_m[-1]
