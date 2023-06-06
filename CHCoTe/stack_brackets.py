def cal_n(line):
    ret = 0
    bracks = ['{','}','[',']','(',')']
    for b in bracks:
        ret += line.count(b)
    return str(ret)
        

def check(line):
    # 스택 초기화
    stack = []
    # 길이만큼 반복하면서 확인
    for char in line:
        # 만약 열린괄호가 온다면 스택에 추가해줌
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
            #n +=1
        # 만약 닫힌 괄호가온다면
        elif char == ')' or char == '}' or char==']':
            if not stack:
                return 0
            elif char == ')' and stack.pop() != '(':
                return 0
            elif char == '}' and stack.pop() != '{':
                return 0
            elif char == ']' and stack.pop() != '[':
                return 0
    # 만약 여는 괄호가 남아있다면 n
    if stack:
        return 0
    return 1
line = list(input())
bool_ = check(line)
if bool_ == 0:
    ans = 'Wrong_'
else:
    ans = 'OK_'

n = cal_n(line)
print(ans+n)

# Type or paste your code in this area
