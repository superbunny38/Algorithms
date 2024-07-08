class Solution:
    def threeSum(self, nums):  
        nums = sorted(nums)
        # print("got:",nums)
        ret = []
        prev_sub_sum = None
        for fixed_idx in range(len(nums)-2):
            left_c, right_c = fixed_idx+1, len(nums)-1
            sub_sum = -nums[fixed_idx]
            if sub_sum == prev_sub_sum:
                continue
            # print()
            # print("@:",-sub_sum, "fixed_idx:",fixed_idx)
            prev_left, prev_right = None, None
            while left_c < right_c and left_c > fixed_idx and right_c < len(nums):
                # print(f"left_c [{left_c}]: {nums[left_c]} right_c [{right_c}]: {nums[right_c]}")
                if sub_sum == nums[left_c] + nums[right_c]:
                    if prev_left != nums[left_c] or prev_right != nums[right_c]:
                        ret.append([nums[fixed_idx],nums[left_c],nums[right_c]])
                        prev_left,prev_right = nums[left_c],nums[right_c]
                    left_c +=1
                    right_c -=1
                    
                elif sub_sum < nums[left_c] + nums[right_c]:
                    right_c -= 1
                else:
                    left_c += 1
            prev_sub_sum = sub_sum
        return ret
