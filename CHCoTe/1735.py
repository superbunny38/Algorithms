#1735
#분수 합
import sys
import copy
input = sys.stdin.readline

def GCD(x,y):
    while y:
        x,y = y,x%y
    return x
            

def sol(numer1,denom1,numer2,denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    div = GCD(numer,denom)
    return int(numer/div),int(denom/div)

numer1, denom1 = map(int,input().split())
numer2, denom2 = map(int, input().split())
a,b = sol(numer1,denom1,numer2,denom2)
print("{} {}".format(a,b))

