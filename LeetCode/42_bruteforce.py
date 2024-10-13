class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        water = height
        for i in range(len(water)):
            left = water[i]

            for check_left_idx in range(i):
                left = max(left,water[check_left_idx])

            right = water[i]
            for check_right_idx in range(i+1,len(water)):
                right = max(right,water[check_right_idx])
            print(f"i:{i} || left {left} right: {right} adding: {min(left,right)-water[i]}")
            res += min(left,right)-water[i]

        return res
