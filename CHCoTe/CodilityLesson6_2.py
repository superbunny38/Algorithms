def solution(A):
    # Implement your solution here
    sorted_A = sorted(A, reverse= True)
    if sorted_A[-2]<0:
        return max([sorted_A[0]*sorted_A[1]*sorted_A[2],sorted_A[-1]*sorted_A[-2]*sorted_A[0]])
    else:
        return sorted_A[0]*sorted_A[1]*sorted_A[2]
    pass
