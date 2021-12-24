#1138
#류채은
#한 줄로 서기
from itertools import permutations
import math

def countleftbig(sets, p):
    count = 0
    i = 0
    while i < p:
        if sets[i] > p:
            count = count + 1
        i = i + 1
    return count

'''
def countleftbig(arr, p, q):
    count = 0
    i = 0
    print("arr",arr)
    print(p,"cm")
    print(q,"번째")
    while i < q:
        print(arr[i])
        if arr[i] > p:
            count = count + 1
        i = i + 1
    return count
'''
while True:
    print("---------\n")
    N = int(input())
    arr = list(map(int,input().split()))
    height = []
    for i in range(N):
        height.append(i+1)
    plz = 0    
    max_count = 0
    sets = list(permutations(height, N))
    possibility = math.factorial(N)
    k = 0   
    print("possibility:",possibility)
    for j in range(possibility):
        while k < N:
            print("sets[j]:",sets[j])
            
            u = 0
            count2 = 0
            while u < k:
                if sets[j][u]>sets[u][k]:
                    count2 = count2 + 1
                u = u + 1
            print("index ",k," 왼 쪽 큰 사람 수:", count2)
            if count2 == arr[k]:
                plz = plz + 1
            else:
                break
            k = k + 1
        if plz == 4:
            print(sets[j])
            break
        
''' 
print("---------\n")
N = int(input())
arr = list(map(int,input().split()))
height = []
for i in range(N):
    height.append(i+1)
plz = 0    
max_count = 0
tmp = list(permutations(height, N))
possibility = math.factorial(N)
print("possibility:",possibility)
for j in range(possibility):
    for q in range(N):
        print("tmp[",j,"]:",tmp[j])
        if countleftbig(tmp[j],tmp[j][q],q) == arr[q]:
            print(q+1,"cm")
            print("countleftbig:",arr[q])
            plz = plz + 1
        else:
            break
    if plz == N:
        print(tmp[j])
#print(tmp)
#print(tmp[0])
#print(tmp[0][0])
'''
