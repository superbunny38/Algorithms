#9012
def split(word):
    return [char for char in word]

def check_valid_VPS(stack):
    remaining_stack = []
    for bracket in stack[::-1]:
        #print("bracket popped from stack:",bracket)
        if len(remaining_stack) == 0:
            remaining_stack.append(bracket)
        else:
            peek = remaining_stack[-1]
            if peek == ')' and bracket == '(':
                #print("pop")
                remaining_stack.pop()
            else:
                remaining_stack.append(bracket)
    
    if len(remaining_stack) == 0:
        return "YES"
    else:
        return "NO"

T = int(input())
strings_stack = []
for _ in range(T):
    strings = input()
    strings_stack.append(split(strings))
    

for idx,stack in enumerate(strings_stack):
    #print("\n\n {}".format(idx))
    #print("".join(stack))
    print(check_valid_VPS(stack))
    
