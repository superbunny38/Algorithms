#15663
#N과 M
from itertools import permutations

n, m = map(int, input().split())
components = list(map(int, input().split()))
components.sort()
ans = list(permutations(components,m))
ans = list(dict.fromkeys(ans))

print(ans)

