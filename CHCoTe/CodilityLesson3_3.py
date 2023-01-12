
def solution(A):
    # Implement your solution here
    for split_idx in range(1,len(A)):
        if split_idx == 1:
            sum1,sum2 = sum(A[:split_idx]),sum(A[split_idx:])
            min_diff = abs(sum1-sum2)
            # print("sum1:",sum1,"sum2:",sum2)
            continue
        move = A[split_idx-1]
        sum1 += move#A[split_idx-1]
        sum2 -= move#A[split_idx-1]
        diff = abs(sum1-sum2)
        # print("moved:",move,"sum1:",sum1,"sum2:",sum2)
        if diff < min_diff:
            min_diff = diff
            # print("sum1:",sum1)
            # print("sum2:",sum2)
    return min_diff
