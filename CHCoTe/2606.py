#2606
#바이러스

import sys
input = sys.stdin.readline
n_computer = int(input())
n_connected = int(input())

graph = dict()
for i in range(n_computer):
    graph[i+1] = []
    
for _ in range(n_connected):
    c1,c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

infected = set()
visited = [False]*(n_computer+1)
query = [1]

while query:
    search = query.pop()
    #print("now on node:",search)
    for adj in graph[search]:
        if visited[adj] == False:
            infected.add(adj)
            query.append(adj)
            visited[adj] = True
    #print("infected:",infected)
            

print(len(infected-set([1])))
