#1764
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
names = dict()
for _ in range(N):
    name = input()[:-1]
    names[name] = True
ans = []
cnt = 0
for _ in range(M):
    name = input()[:-1]
    if name in names:
        ans.append(name)
        cnt+=1

print(cnt)
ans = sorted(ans)
#print(ans)
for an in ans:
    print(an)
