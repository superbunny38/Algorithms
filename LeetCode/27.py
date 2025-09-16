class Solution:
    def removeElement(self, nums, val):
        k = 0
        for idx in range(len(nums)-1,-1,-1):
            print("on nums[idx]:",nums[idx])
            if nums[idx] == val:
                nums.pop(idx)
                nums.append('_')
                
            else:
                k+=1
        print("nums:",nums)
        return k
    
s = Solution().removeElement(nums = [3,2,2,3], val = 3)
print(s)