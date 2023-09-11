#9663
#N-Queen
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
graph = [0]*N
total_cnt = 0

def is_possible(cur_row):
    for row_idx in range(cur_row):
        if abs(graph[row_idx]-graph[cur_row]) == abs(row_idx-cur_row):
            return False
        if graph[row_idx] == graph[cur_row]:
            return False
    return True

def n_queen(start_level):
    global total_cnt
    if start_level == N:
        total_cnt +=1
        return
    else:
        for i in range(N):
            graph[start_level] = i
            if is_possible(start_level):
                n_queen(start_level+1)

n_queen(0)       
print(total_cnt)
