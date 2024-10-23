class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for num_idx in range(1,len(nums)):
            cur_val = nums[num_idx]
            
            if cur_val>ans[-1]:
                ans.append(cur_val)
            else:
                low, high = 0, len(ans)-1
                while low<high:
                    mid = low + (high-low)//2
                    if ans[mid]<cur_val:
                        low = mid+1
                    else:
                        high = mid
                ans[low] = cur_val
        return len(ans)
                    
