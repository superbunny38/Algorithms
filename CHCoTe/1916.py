#최소비용 구하기
#류채은
#다익스트라
import sys
import heapq
import math

input = sys.stdin.readline

N = int(input())#도시의 개수
M = int(input())#버스의 개수
graph =[[] for _ in range(N+1)]
distance = [math.inf]*(N+1)


for _ in range(M):
    start_,end_,cost_ = map(int, input().split())
    graph[start_].append((end_,cost_))
start,end = map(int,input().split())
#print("graph:")
#print(graph)


#finding shortest distance#

q = []
heapq.heappush(q,(0,start))
distance[start] = 0

while q:
    cost, dest = heapq.heappop(q)
    #print("cost:",cost,"dest:",dest)
    if distance[dest] < cost:
        continue
    for adj in graph[dest]:
        tmp_cost = distance[dest] + adj[1]
        if tmp_cost < distance[adj[0]]:
            distance[adj[0]] = tmp_cost
            heapq.heappush(q,(tmp_cost,adj[0]))

print(distance[end])

#########################
