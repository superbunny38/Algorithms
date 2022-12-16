# 사전

def check_loc(num_list,K):
    return_idx = 0
    if num_list[0] > K:
        return -1
    
    for idx, value in enumerate(num_list):
        if value <= K:
            return_idx = idx

    return return_idx

N, K = map(int, input().split())
num_list = [int(x) for x in input().split()]
ret = check_loc(num_list,K)
print(f" {ret}")

# Type or paste your code in this area
