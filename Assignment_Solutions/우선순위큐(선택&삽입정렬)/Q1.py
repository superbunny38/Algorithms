# Type or paste your code in this area
n = int(input())
L = [int(item) for item in input().split()]

for pass_ in range(n-1,-1,-1):
    maxLoc = pass_
    for j in range(0,pass_,1):
        if L[j] > L[maxLoc]:
            maxLoc = j
    L[pass_],L[maxLoc] = L[maxLoc],L[pass_]

for elem in L:
    print(f" {elem}", end = "")
