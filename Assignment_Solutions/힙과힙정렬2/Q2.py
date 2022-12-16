from heapq import heapify, heappop
n = int(input())
numbers = list(map(int,input().strip().split()))[:n]
heapify(numbers)

for _ in range(n):
    if _ != n-1:
        print(f" {heappop(numbers)}", end = "")
    else:
        print(f" {heappop(numbers)}")
# Type or paste your code in this area
