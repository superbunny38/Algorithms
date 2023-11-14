#1966
#프린터 큐

import heapq
import sys
input = sys.stdin.readline

N_test = int(input())
for test_id in range(N_test):
    N,M = map(int,input().split())
    count = 0
    weights_ = list(map(int, input().split()))
    q = []
    
    for idx in range(N):
        q.append((idx,weights_[idx]))

    n_print = 0
    while True:
        dequeued = q.pop(0)
        idx,w = dequeued[0],dequeued[1]
        
        if w != max(weights_):
            q.append(dequeued)
            continue
        else:
            n_print +=1
            weights_.remove(w)
            
        if M == idx:
            print(n_print)
            break
            
        
