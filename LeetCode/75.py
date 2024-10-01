class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        else:
            right_idx = 1
            while right_idx < len(nums):
                left_idx = right_idx-1
                cur_val = nums[right_idx]
                while left_idx >= 0 and cur_val<nums[left_idx]:
                    nums[left_idx+1] = nums[left_idx]
                    left_idx -=1
                nums[left_idx+1] = cur_val
                right_idx +=1
            return nums



        
