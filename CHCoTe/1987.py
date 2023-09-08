#1987
#알파벳
#류채은
#그래프

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

R,C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

visited_q = set([(0,0,graph[0][0])])

max_cnt = 0
dx,dy = [0,0,1,-1],[1,-1,0,0]

def bfs(visited_q):
    global max_cnt
    while visited_q:
        y,x,path = visited_q.pop()
        if max_cnt < len(path):
            max_cnt = len(path)
        for move_x, move_y in zip(dx,dy):
            if 0<=x+move_x<C and 0<=y+move_y<R and graph[y+move_y][x+move_x] not in path:
                visited_q.add((y+move_y,x+move_x,path+graph[y+move_y][x+move_x]))
        
     
bfs(visited_q)   
print(max_cnt)
