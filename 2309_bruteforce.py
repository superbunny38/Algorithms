#2309
from itertools import permutations

heights = []
for i in range(9):
    k = int(input())
    heights.append(k)

emit = list(permutations(heights,2))
for em in emit:
    if sum(heights) - sum(list(em)) == 100:
        answer = [item for item in heights if item not in em]
        answer.sort()
        for mem in answer:
            print(mem)
        break
