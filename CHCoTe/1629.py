#1629
import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

def solution(a,b,c):
    if b == 0:
        return 1
    elif b == 1:
        return a%c
    
    k = solution(a,b//2,c)
    if (b%2) == 0:
        return (k**2)%c
    else:
        return ((k**2)%c*a)%c

A,B,C = map(int, input().split())
print(solution(A,B,C))
