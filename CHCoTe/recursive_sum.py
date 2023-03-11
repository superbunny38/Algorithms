import sys
sys.setrecursionlimit(10**6)
def recurs_sum(N):
    if N<2:
        return N
    else:
        return N+recurs_sum(N-1)



n = int(input())
print(recurs_sum(n))
