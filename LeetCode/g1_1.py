class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()#key: number, val: index
        for idx, num in enumerate(nums):
            find = target-num
            if find in store:
                return [store[find],idx]
            else:
                store[num] = idx
