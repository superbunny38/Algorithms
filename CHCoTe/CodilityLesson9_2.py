# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    dp = []
    for idx in range(len(A)):
        if idx ==0:
            dp.append(A[0])
        else:
            cur_dp = max(A[idx],dp[idx-1]+A[idx])
            dp.append(cur_dp)
    return max(dp)
