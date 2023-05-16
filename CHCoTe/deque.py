from collections import deque

def exoj_print(dq):
    for idx,val in enumerate(dq):
        if idx == len(dq)-1:
            print(f" {val}")
        else:
            print(f" {val}",end = "")

deq = deque()


N = int(input())
for _ in range(N):
    orders = input().split()
    order = orders[0]
    if order == 'AF':
        item = orders[1]
        deq.appendleft(item)
    elif order == 'AR':
        item = orders[1]
        deq.append(item)
    elif order == 'DF':
        try:
            deq.popleft()
        except:
            print("underflow")
            break
    elif order == 'DR':
        try:
            deq.pop()
        except:
            print("underflow")
            break
    elif order == 'P':
        exoj_print(deq)
