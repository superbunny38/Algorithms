#16236
import sys
import copy
input = sys.stdin.readline

N = int(input())
graph = []
for c_idx in range(N):
    r = list(input().split())
    r = [int(x) for x in r]
    if 9 in r:
        shark_y, shark_x = c_idx, r.index(9)#상어 위치 표기
    graph.append(r)

#위, 왼, 오, 아래
dx = [0,-1,1,0]
dy = [-1,0,0,1]

shark_size = 2
need_to_eat = copy.deepcopy(shark_size)
    

def eat_possible(graph):
    global N, shark_y, shark_x, shark_size, need_to_eat
    cur_y,cur_x = shark_y,shark_x
    visited = [[0]*N for _ in range(N)]
    queue = [[shark_y,shark_x]]
    possible_list = []
    #print("Initially:")
    #for g in graph:
    #    print(g)
    graph[shark_y][shark_x] = 0
    while queue:
        loc = queue.pop(0)
        cur_y,cur_x = loc[0],loc[1]
        #print(f"\ncurrently at: ({cur_y},{cur_x})")
        if graph[cur_y][cur_x] == shark_size:
            #print("pass")
            pass
        elif graph[cur_y][cur_x]!= 0 and graph[cur_y][cur_x] < shark_size:
            #print(f"ate shark of size {graph[cur_y][cur_x]} at ({cur_y},{cur_x})")
            possible_list.append([visited[cur_y][cur_x],cur_y,cur_x])
            
        
        for move_y,move_x in zip(dy,dx):
            if 0<=cur_y+move_y<N and 0<=cur_x+move_x<N and visited[cur_y+move_y][cur_x+move_x]==0:
                if graph[cur_y+move_y][cur_x+move_x] <= shark_size:
                    visited[cur_y+move_y][cur_x+move_x] = visited[cur_y][cur_x]+1
                    queue.append([cur_y+move_y,cur_x+move_x])
        #for v in visited:
        #    print(v)
    return sorted(possible_list,key = lambda x: (x[0],x[1],x[2]))


def eat(graph):
    global N, shark_y, shark_x, shark_size, need_to_eat
    possible = eat_possible(graph)
    if possible:
        ret = possible[0]
        moved = ret[0]
        shark_y,shark_x = ret[1],ret[2]
        need_to_eat -= 1
        if need_to_eat == 0:
            shark_size +=1
            need_to_eat = copy.deepcopy(shark_size)
        #print(f"shark size:{shark_size} need to eat more: {need_to_eat}")
        graph[shark_y][shark_x] = 9
        return moved
    else:
        return 0

def solution(graph):
    global N, shark_y, shark_x, shark_size, need_to_eat
    
    elapsed = 0
    ret = 99
    while ret != 0:
        ret = eat(graph)
        elapsed += ret
        #print(f">> elapsed: {elapsed} (+{ret})\n\n")
        if ret == 0:
            return elapsed

print(solution(graph))
