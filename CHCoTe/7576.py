from collections import deque
import sys
input = sys.stdin.readline

def count_zeros(graph):
    n_zeros = 0
    where_ones = deque([])
    w,h = len(graph[0]),len(graph)

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                where_ones.append((i,j))
            elif graph[i][j] == 0:
                n_zeros+=1
                
    return n_zeros, where_ones


def elapse(graph,deque,prev_n_zeros,visited):
    new_n_ones = 0
    
    w,h = len(graph[0]),len(graph)
    

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    prev_n_count_ones = len(deque)
    
    for idx in range(prev_n_count_ones):
        where_one = deque.popleft()
        one_y,one_x = where_one[0],where_one[1]
        
            
        for move_y, move_x in zip(dy,dx):
            candi_y,candi_x = one_y+move_y, one_x+move_x
                
            if 0<=candi_y<h and 0<=candi_x<w:
                if graph[candi_y][candi_x] == 0 and visited[candi_y][candi_x] == 0:
                    deque.append((candi_y,candi_x))
                    graph[candi_y][candi_x] = 1
                    new_n_ones += 1
                    visited[one_y][one_x] = 1
            
    return prev_n_zeros - new_n_ones


def solution(graph,w,h):
    day_count = 0
    n_zeros, where_ones = count_zeros(graph)
    if n_zeros == 0:
        return day_count
    prev_n_zeros = n_zeros
    visited = [[0 for _ in range(w)] for tmp in range(h)]
    while True:
        n_zeros = elapse(graph,where_ones, prev_n_zeros,visited)
        day_count +=1

        if n_zeros == 0:
            return day_count
        if n_zeros == prev_n_zeros:
            return -1
        prev_n_zeros = n_zeros
        


w,h = map(int, input().split())
graph = []
for g in range(h):
    graph.append([int(x) for x in list(input().split())])


print(solution(graph,w,h))
