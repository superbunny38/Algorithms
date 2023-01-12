def solution(A):
    # Implement your solution here
    save_dict = dict()
    
    for a in A:
        save_dict[a] = 1
    
    for num in range(1,len(A)+1):
        if num not in save_dict:
            return 0
    return 1
