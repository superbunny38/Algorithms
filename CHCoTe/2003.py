#2003
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A= list(map(int,input().split()))

start_idx,end_idx = 0,1
count = 0

while start_idx<end_idx and end_idx<=N:
    #print(f"checking... start_idx: {start_idx} end_idx: {end_idx}")
    cumsum = sum(A[start_idx:end_idx])
    if cumsum < M:
        end_idx +=1
    elif cumsum == M:
        #print(f"A[{start_idx}:{end_idx}]")
        end_idx +=1
        count+=1
    else:#cumsum>M
        start_idx+=1
        end_idx = start_idx +1
print(count)
