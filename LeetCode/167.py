class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1,n = 0,len(numbers)
        idx2 = n-1
        while idx1<idx2:
            cur_sum = numbers[idx1] + numbers[idx2]
            if cur_sum == target:
                return [idx1+1,idx2+1]
            elif cur_sum < target:
                idx1 += 1
            else:
                idx2 -=1
        
        
