#1138
#류채은
#1138
#한 줄로 서기
from itertools import permutations

def nleftsideTall(sets, a, index):
    i = 0
    count = 0
    while i < index:
        if sets[i] > a:
            count = count + 1
        i = i + 1
    return count
    

height = []
N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    height.append(i+1)

sets = list(permutations(height, N))
for i in range(len(sets)):
    plz = 0
    for j in range(N):
        #print(sets[i][j],"-",end="")
        a = sets[i][j]
        if arr[a-1] == nleftsideTall(sets[i],sets[i][j],j):
            #print(a)
            plz = plz + 1
        else:
            break
    #print(">>plz(+):",plz)    
    if plz == N:
        answer = sets[i]
        break
for k in range(N):
    print(answer[k],end=" ")

    
