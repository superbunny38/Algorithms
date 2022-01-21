#1927
from ImportHeapPriorityQueue import *
N = int(input())
orders = []
for i in range(N):
    o = int(input())
    orders.append(o)

HPQ = HeapPriorityQueue()
for order in orders:
    if order == 0:
        if HPQ.is_empty():
            print(0)
        else:
            print(HPQ.min()[0])
            HPQ.remove_min()
    else:
        HPQ.add(order,"")
