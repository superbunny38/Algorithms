class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestDiffSoFar,n = 10**6,len(nums)
        nums.sort()
        
        if n == 3:
            return sum(nums)

        for a_idx, a in enumerate(nums):
            if a_idx>0 and nums[a_idx-1] == a:
                continue

            # print(f"a_idx:{a_idx} a:{a}")
            idx1, idx2 = a_idx+1, n-1

            while idx1<idx2:
                curSum = a+nums[idx1]+nums[idx2]
                diff = abs(curSum-target)

                if curSum == target:
                    return target

                if diff == 0:
                    return target

                if diff < closestDiffSoFar:
                    ret = curSum
                    closestDiffSoFar = diff

                if curSum>target:
                    idx2 -= 1
                elif curSum<target:
                    idx1 += 1
                else:
                    return target
                
        return ret

