def matching(peek,s):
    if s == ')':
        if peek == '(':
            return True
        else:
            return False
    elif s == '}':
        if peek == '{':
            return True
        else:
            return False
    elif s == ']':
        if peek == '[':
            return True
        else:
            return False


def solution(S):
    # Implement your solution here
    stack = []
    if len(S) == 0:#empty
        return 1
    for s in S:
        if len(stack) == 0:
            stack.append(s)
        else:
            peek = stack[-1]
            if matching(peek, s) == True:
                stack.pop(-1)
            else:
                stack.append(s)
    if len(stack) == 0:
        return 1
    else:
        return 0
            
    pass
