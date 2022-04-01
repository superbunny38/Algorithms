import sys, heapq


v, e=input().split()
v, e = int(v),int(e)

visited=[0]*(v+1)

lst=[[] for _ in range(v+1)]
ans=0

for _ in range(e) :
    a, b, c=input().split()
    a,b,c = int(a),int(b),int(c)
    lst[a].append([c,b])
    lst[b].append([c,a])

que=[(0,1)]     
while que :
    node=heapq.heappop(que)
    if not visited[node[1]] :
        visited[node[1]]=1
        ans+=node[0]
        for n in lst[node[1]] :
            heapq.heappush(que, n)

print(ans)
