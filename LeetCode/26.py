class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print("\n\n")
        print("len(nums):",len(nums))
        # dump = []
        track_idx = 1
        
        for idx, num in enumerate(nums):
            if idx == 0:
                cur = num
            else:        
                cur = nums[track_idx-1]        
                if cur == num:
                    continue
                else:
                    cur = num
                    print(f"insert {cur} at {track_idx}")
                    nums.insert(track_idx,cur)
                    track_idx +=1
        print("k:",track_idx)
        print(nums)
        return track_idx
