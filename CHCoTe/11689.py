#11689
import sys
import copy
input = sys.stdin.readline
N = int(input())
ret = copy.deepcopy(N)

def euler(n):
    global ret
    for div in range(2,int(n**(1/2))+1):
        if n%div == 0:
            while n%div == 0:
                n//=div
            ret *= (1-1/div)

    if n>1:
        ret *= (1-1/n)
    return int(ret)

print(euler(N))
            
