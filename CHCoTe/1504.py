#1504
#특정한 최단 경로

import sys
import math
import heapq
input = sys.stdin.readline

N,E= map(int, input().split())
graph = dict()
for node in range(N):
    graph[node+1] = []

for _ in range(E):
    a,b,c, = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int,input().split())

## start -> v1 -> v2 -> end
## start -> v2 -> v1 -> end

START = 1
END = N
INF = math.inf

def dijikstra(start, end):
    if start == end:
        return 0
    global INF
    distance = [INF]*(N+1)
    q = []
    heapq.heappush(q,(0,start))#순서: 비용, 노드
    while q:
        cost, cur = heapq.heappop(q)

        if distance[cur] < cost:
            continue

        for adj in graph[cur]:
            tmp_cost = adj[1] + cost
            if tmp_cost < distance[adj[0]]:
                distance[adj[0]] = tmp_cost
                heapq.heappush(q, (tmp_cost, adj[0]))
    return distance[end]

path1 = dijikstra(START,v1)+dijikstra(v1,v2)+dijikstra(v2,END)
#print(f"path1: {dijikstra(START,v1)}({START}->{v1})+{dijikstra(v1,v2)}+{dijikstra(v2,END)} == {path1}")
path2 = dijikstra(START,v2)+dijikstra(v2,v1)+dijikstra(v1,END)
#print(f"path2: {dijikstra(START,v2)}+{dijikstra(v2,v1)}+{dijikstra(v1,END)} == {path2}")

def is_path(path):
    global INF
    if path >= INF:
        return -1
    else:
        return path
print(is_path(min(path1,path2)))
