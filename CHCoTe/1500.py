#1500
#최대곱

#import copy
import sys
input = sys.stdin.readline

S,K = map(int, input().split())

def sol(s,k):
    mid = s//k
    remainder = s%k
    if mid == 1:
        mid = 2
        n_ones = mid*k-s
        return 2**(k-n_ones)
        
        
    num = 1
    #mul = []
    for i in range(k):
        if i!=k-1:
            if remainder > 0:
                s-=(mid+1)
                remainder -=1
                num*=(mid+1)
            else:
                s -= mid
                num*=mid
                #mul.append(mid)
        else:
            num*=s
            #mul.append(s)
            s = 0
    #print(mul)
    return num

print(sol(S,K))
        
        
        
