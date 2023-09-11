#1912
import sys
input = sys.stdin.readline

n = int(input())
num_list = input().split()
num_list = [int(x) for x in num_list]

def get_max_cum_sum(num_list):
    memoization = []
    for idx,num in enumerate(num_list):
        if idx == 0:
            memoization.append(num)
            continue
        cur = max(num,memoization[idx-1]+num)
        memoization.append(cur)
    return max(memoization)

print(get_max_cum_sum(num_list))
