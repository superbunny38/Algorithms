class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x_candi in range(max(nums)+1):
            count = 0
            for num in nums:
                if num >= x_candi:
                    count +=1
            if count == x_candi:
                return count
        return -1
