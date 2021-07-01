#10819
from itertools import permutations

def sum_function(num_list):
    prev = num_list[0]
    result = 0
    for i in range(len(num_list)-1):
        result += abs(prev - num_list[i+1])
        prev = num_list[i+1]
    return result

#입력받기
n = int(input())
li = list(map(int,input().strip().split()))[:n]#입력받은 리스트

permu = list(permutations(li))

maxi = 0
for p in permu:
    tmp_sum = sum_function(p)
    if tmp_sum > maxi:
        maxi = tmp_sum

print(maxi)


