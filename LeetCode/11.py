class Solution:
    def maxArea(self, height: List[int]) -> int:
        # List = height
        List = [0]+height
        max_area = 0
        left_pointer, right_pointer = 1, len(List)-1
        while left_pointer < right_pointer:
            left_height = List[left_pointer]
            right_height = List[right_pointer]
            cur_area = (right_pointer-left_pointer)*min(left_height,right_height)
            max_area = max(cur_area,max_area)
            if left_height < right_height:
                left_pointer +=1
            else:
                right_pointer -=1
                
        return max_area
