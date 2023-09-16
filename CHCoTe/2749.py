#2749
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
#피보나치의 주기는 1500000이다..ㅎㅎ

n = int(input())
memoization = [0,1]
def fibo(N):
    for i in range(1500000):
        tmp = memoization[i]+memoization[i+1]
        memoization.append(tmp%1000000)
    return memoization[N%1500000]


print(fibo(n))
