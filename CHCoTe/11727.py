#2xn 타일링 2
import sys
sys.setrecursionlimit(10**6)

def get_n_tiles(n):
    memoization = [0,1,3]
    if n<=2:
        return memoization[n]
    else:
        for i in range(3,n+1):
            val = memoization[i-1]+memoization[i-2]*2
            memoization.append(val)
    return memoization[n]
    
n = int(sys.stdin.readline())
print(get_n_tiles(n)%10007)
