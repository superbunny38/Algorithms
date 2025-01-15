class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        n = len(nums)

        for a_idx, a in enumerate(nums):
            if a_idx > 0 and a == nums[a_idx-1]:
                continue
            idx1 = a_idx+1
            idx2 = n-1
            while idx1<idx2:
                cur_sum = a + nums[idx1]+nums[idx2]
                if cur_sum == 0:
                    ret.append([a,nums[idx1],nums[idx2]])
                    idx1 += 1
                    while nums[idx1-1] == nums[idx1] and idx1<idx2:
                        idx1 +=1
                elif cur_sum < 0:
                    idx1 +=1
                else:
                    idx2 -=1
        return ret
            
        
