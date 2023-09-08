#1987
#알파벳
#류채은
#그래프

import sys
input = sys.stdin.readline

R,C = map(int, input().split())
graph = []
for _ in range(R):
    tmp = list(input())[:C]
    graph.append(tmp)

visited = set()

max_cnt = 0

def dfs(x,y,cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    for move_x, move_y in zip(dx,dy):
        if 0<=x+move_x<C and 0<=y+move_y<R and graph[y+move_y][x+move_x] not in visited:
            visited.add(graph[y+move_y][x+move_x])
            dfs(x+move_x,y+move_y,cnt+1)
            visited.remove(graph[y+move_y][x+move_x])

visited.add(graph[0][0])    
dfs(0,0,1)   
print(max_cnt)
