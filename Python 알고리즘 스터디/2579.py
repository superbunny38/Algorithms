#2579
#계단오르기
#류채은

def ans(stairs, n):
    dp = []
    dp.append(stairs[0])
    a = 1
    while a< 3:
        if a == 1:
            dp.append(max(dp[a-1]+stairs[a], stairs[a]))
            continue
        dp.append(max(dp[a-2] +stairs[a], stairs[a-1] + stairs[a]))
        a = a+ 1
    b = 3
    while b < n:
        dp.append(max(stairs[b] + stairs[b-1] + dp[b-3], stairs[b] + dp[b-2]))
        b = b + 1

    print(dp[-1])

stairs = []

n = int(input())
for i in range(n):
    tmp = int(input())
    stairs.append(tmp)
#print("print")
print(ans(stairs, n))
