def solution(A):
    # Implement your solution here
    # save_A = dict()
    count_1 = 0
    save_zero_idxs = dict()
    for idx,a in enumerate(A):
        if a == 1 and save_zero_idxs:
            count_1+=1
        if a == 0:
            save_zero_idxs[idx] = - count_1
    ret= 0
    # print("save:",save_zero_idxs)
    # print("count 1:",count_1)

    for value in list(save_zero_idxs.values()):
        ret = ret + count_1 + value
        if ret > 1000000000:
            return -1    
    return ret
