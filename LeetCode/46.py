import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        if len(nums) == 1:
            return [nums]

        def generate(ans, remaining):
            if len(remaining) == 1:
                ret.append(ans+remaining)
                return
            
            for remain in remaining:
                tmp_remaining = copy.deepcopy(remaining)
                tmp_remaining.remove(remain)
                generate(ans+[remain],tmp_remaining)
            
        
        for idx,num in enumerate(nums):
            tmp_nums = copy.deepcopy(nums)
            tmp_nums.remove(num)
            generate([num], tmp_nums)    
            
        return ret
