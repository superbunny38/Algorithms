# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if len(A) == 0:
        return A
    
    for _ in range(K):
        move = A.pop(-1)
        A = [move]+A
    return A
    pass
