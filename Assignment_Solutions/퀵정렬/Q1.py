def ex_oj_print(L):
    length = len(L)
    for idx, num in enumerate(L):
        if idx == length -1:
            print(f" {num}")
        else:
            print(f" {num}",end = "")

N = int(input())
num_list = [int(x) for x in input().split()]
ex_oj_print(sorted(num_list))
# Type or paste your code in this area
