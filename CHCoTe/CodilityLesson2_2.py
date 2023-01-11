def solution(A):
    # Implement your solution here
    save = dict()
    for num in A:
        if num not in save:
            save[num] = 1
        elif save[num] == 1:
            del save[num]
    
    return list(save.keys())[0]
    pass
