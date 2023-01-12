# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    save_a = dict()
    max_ = 0
    max_idx = 0
    N = len(A)
    if N == 1:
        return 0
    for idx,a in enumerate(A):
        if a not in save_a:
            save_a[a] = 1
        else:
            save_a[a] +=1
            if save_a[a] > max_:
                max_ = save_a[a]
                max_idx = idx
    
    if N/2<max_:
        return max_idx
    return -1
