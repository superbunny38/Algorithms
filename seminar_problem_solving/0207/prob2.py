from heapq import heappush, heappop

n = int(input())
m = int(input())
inf = 999

s = [[] for i in range(n + 1)]
dp = [inf for i in range(n + 1)]
for i in range(m):
    a, b, w = input().split()
    a,b,w = int(a),int(b),int(w)
    s[a].append([b, w])
start, end = map(int, input().split())
def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        for n_n, wei in s[n]:
            n_w = w + wei
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
dijkstra(start)
print(dp[end])
