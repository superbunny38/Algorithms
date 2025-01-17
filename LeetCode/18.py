class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        n = len(nums)
        if n == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return ret

        nums.sort()
        
        # print(nums)
        for a_idx, a in enumerate(nums[:-3]):
            if a_idx>0 and a==nums[a_idx-1]:
                continue
            # print(f"a_idx:{a_idx} a:{a}")
            for b_idx,b in enumerate(nums[a_idx+1:-2]):
                if b_idx>0 and b == nums[a_idx+1+b_idx-1]:
                    continue
                # print(f"b_idx:{b_idx} b:{b}")
                l_idx, r_idx = a_idx+b_idx+2, n-1
                firsttwoSum = nums[a_idx]+nums[b_idx+a_idx+1]
                # print("firsttwoSum:",firsttwoSum)
                
                while l_idx<r_idx:
                    # print("l_idx:",l_idx,"r_idx:",r_idx)
                    curSum = firsttwoSum + nums[l_idx]+nums[r_idx]
                    if curSum == target:
                        ret.append([nums[a_idx],nums[a_idx+b_idx+1],nums[l_idx],nums[r_idx]])
                        l_idx +=1
                        while nums[l_idx-1] == nums[l_idx] and l_idx<r_idx:
                            l_idx += 1

                        r_idx -=1
                        while nums[r_idx+1] == nums[r_idx] and l_idx<r_idx:
                            r_idx -=1
                        
                    elif curSum < target:
                        l_idx +=1
                    else:
                        r_idx -=1
        return ret
