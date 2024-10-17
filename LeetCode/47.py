import copy
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        set_nums = Counter(nums)
        ans = []
        print("set_nums:",set_nums)
        def generate_permu(sofar,left):
            if sum(left.values()) == 1:
                ans.append(sofar+list(left.keys()))
            else:
                for l in left.keys():
                    tmp_left = copy.deepcopy(left)
                    if tmp_left[l] == 1:
                        del tmp_left[l]
                    else:
                        tmp_left[l] -= 1
                    generate_permu(sofar+[l],tmp_left)

        for num in set_nums.keys():
            tmp_set_nums = copy.deepcopy(set_nums)
            if set_nums[num] == 1:
                del tmp_set_nums[num]
            else:
                tmp_set_nums[num] -= 1
            generate_permu([num],tmp_set_nums)
        return ans
