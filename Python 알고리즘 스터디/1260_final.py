from collections import deque

def dfs(v):
    print(v, end='')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and adj[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    visit[v] = 1
    queue.append(v)

    while (queue):
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if visit[i] == 0 and adj[v][i] == 1:
                queue.append(i)
                visit[i] = 1

n, m, v = map(int, input().split())#n:정점의 개수m:간선의 개수 v:탐색시작정점번호

adj = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1

dfs(v)
print()

visit = [0 for i in range(n+1)]
bfs(v)
