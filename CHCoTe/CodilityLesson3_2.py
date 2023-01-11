# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A) == 0:
        return 1

    save_A = dict()
    for num in A:
        save_A[num] = 0
    
    for n in range(1,len(A)+2):
        if n not in save_A:
            return n

    pass
