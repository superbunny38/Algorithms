class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        start = ['(']
        ans = []
        while start:
            popped = start.pop(0)
            #left
            if popped.count('(') == n and popped.count(')')==n:
                ans.append(popped)
                continue
            if popped.count('(') < n:
                left_node = popped + '('
                start.append(left_node)
            #right
            if popped.count(')') < n and popped.count(')') < popped.count('('):
                right_node = popped + ')'
                start.append(right_node)
        return ans
            

            
