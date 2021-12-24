#2220
#류채은
#힙 정렬
from itertools import permutations

n = int(input())
a = []
i = 1
while i < n:
    j = i
    while j > 1:
        a[j] = a[j/2]
        j = j / 2
    a[1] = i + 1
    i = i + 1

a[n] = 1

k = 1
while k <= n:
    print(a[k], end=" ")
    k = k + 1
