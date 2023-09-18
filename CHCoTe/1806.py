#1806
import sys
import math
input = sys.stdin.readline
N,M = map(int,input().split())
A= list(map(int,input().split()))

start_idx,end_idx = 0,0
min_dist = math.inf
sum = 0

while end_idx<N+1:
    #print(f"checking... start_idx: {start_idx} end_idx: {end_idx}")
    
    if sum < M:
        #print("<")
        try:
            sum += A[end_idx]
            end_idx +=1
        except:
            break
    elif sum >= M:
        #print(">=")
        dist = end_idx-start_idx
        if dist == 1:
            min_dist = 1
            break
        if min_dist > dist:
            min_dist= dist
            #print(f"gotcha: A[{start_idx}:{end_idx}]")
        
        sum -= A[start_idx]
        start_idx +=1
        
if min_dist == math.inf:
    print(0)
else:
    print(min_dist)
