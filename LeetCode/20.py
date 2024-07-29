class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'}':'{',  ']':'[', ')':'('}
        for bracket in s:
            print("\nbracket;",bracket)
            if bracket == '(' or bracket == '{' or bracket == '[':
                print("opening")
                stack.append(bracket)
            else:
                print("closing")
                print("matching:",matching)
                if stack and stack[-1] == matching[bracket]:
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True
