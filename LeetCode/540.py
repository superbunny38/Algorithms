class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return 0
        else:
            mid_idx = int(len(nums)//2)
            left = nums[mid_idx-1]
            right = nums[mid_idx+1]
            
            print("mid_idx:",mid_idx)
            if left != nums[mid_idx] and right != nums[mid_idx]:
                return nums[mid_idx]
            
            elif left == nums[mid_idx] and right != nums[mid_idx]:
                if len(nums) == 3:
                    return right
                else:
                    return self.singleNonDuplicate(nums[:mid_idx-1]) + self.singleNonDuplicate(nums[mid_idx+1:])
            elif right == nums[mid_idx] and left != nums[mid_idx]:
                if len(nums) == 3:
                    return left
                else:
                    return self.singleNonDuplicate(nums[:mid_idx])+self.singleNonDuplicate(nums[mid_idx+2:])
            else:
                print("error")
