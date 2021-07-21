#10828
#스택

def push(stack,num):
    #print("push")
    stack.append(num)
    return stack

def empty(stack):
    #print("is empty")
    if len(stack) == 0:
        #print("empty")
        return 1
    else:

        #print("not empty: ",stack)
        return 0

def pop(stack):
    #print("pop")
    if empty(stack):
        return stack, -1

    else:
            
        output = stack[-1]
        stack.pop(len(stack)-1)
        return stack, output

def size(stack):
    #print("size")
    return len(stack)

        
def top(stack):
    #print("top")
    if empty(stack):
        return -1
    else:
        return stack[-1]

n_orders = int(input())
stack = []
orders = []
for _ in range(n_orders):
    t = input()
    orders.append(t)
    

for order in orders:        
    tmp = order
    if " " in tmp:
        #print("공백 있음")
        order, n = tmp.split()
        
    else:
        #print("공백없음")
        order = tmp

    if order == 'push':
        stack = push(stack,n)
        
    elif order == 'pop':
        stack, output = pop(stack)
        print(output)

    elif order == 'size':
        print(size(stack))

    elif order == 'empty':
        print(empty(stack))

    elif order == 'top':
        print(top(stack))
