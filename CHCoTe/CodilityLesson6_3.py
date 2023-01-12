# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def is_traingular(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    return False

def solution(A):
    # Implement your solution here
    sorted_A = sorted(A)
    # print(sorted_A)
    for i in range(len(A)-2):
        for j in range(i+1,len(A)-1):
            next_idx = j+1
            # print(f"on mark:{sorted_A[i]}, {sorted_A[j]}, {sorted_A[next_idx]}")
            if is_traingular(sorted_A[i],sorted_A[j],sorted_A[next_idx]) == True:
                # print(f"triangular:{sorted_A[i]}, {sorted_A[j]}, {sorted_A[next_idx]}")
                return 1
            break
    return 0
