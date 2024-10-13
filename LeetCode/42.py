class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        rMax = height[-1]
        right = len(height)-2
        lMax = height[0]
        left = 1

        while left<=right:
            if lMax<=rMax:
                res += max(0,lMax-height[left])
                lMax = max(lMax,height[left])
                left+=1
                
            else:
                res += max(0,rMax-height[right])
                rMax = max(height[right],rMax)
                right -=1

        return res
