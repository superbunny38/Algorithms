#2785_2

N = int(input())
L = list(map(int,input().split()))

L.sort()
s = L[0]
for i in range(N):
    cnt = N - i - 1
    s += L[i]
    if s>= cnt:
        print(cnt)
        break
