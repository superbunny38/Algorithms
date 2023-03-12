import sys
sys.setrecursionlimit(10**6)

def order_rev_print(n):
    if n < 10:
        print(n)
    else:
        print(n%10)
        order_rev_print(n//10)

N = int(input())
order_rev_print(N)
