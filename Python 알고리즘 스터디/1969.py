#1969
#DNA
#류채은
from collections import Counter

def modefinder(sequence):
    c = Counter(sequence)
    mode = c.most_common(1)
    return mode[0][0]


def split(word): 
    return [char for char in word]

def HDistance(arr1,arr2):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count = count + 1
    return count

N, M = map(int,input().split())
dna=[]

for i in range(N):
    #line = []
    tmp = input()
    dna.append(split(tmp))
    #line.append(split(tmp))    
    #dna.append(line)
#print(">>dna:\n",dna)

dna_arr = []

for j in range(M):
    line2 = []
    for l in range(N):
        
        line2.append(dna[l][j])
        #print("dna[l][j]",dna[l][j])
    #print("line2:",line2)
    dna_arr.append(line2)
        #dna_arr.append([dna[l][j]])#list
for q in range(M):
    #print(dna_arr[q])
    dna_arr[q].sort()
#print(dna_arr)
final = []
for t in range(M):
    final.append(modefinder(dna_arr[t]))
sum_hd = 0
#print("final:",final)
for b in range(N):
    sum_hd = sum_hd + HDistance(dna[b],final)
print("".join(final))
print(sum_hd)


#print(dna_arr)
'''
print("sum_hd",sum_hd)
mini, index = findMin(sum_hd)

print(dna[index])
print(mini)

'''
