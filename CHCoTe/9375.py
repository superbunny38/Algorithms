import sys
input = sys.stdin.readline

def sol(closet_):
    ans = 1
    for key, value in closet_.items():
        ans = ans*(len(value)+1)
    ans -=1
    print(ans)
    
n_tc = int(input())


for _ in range(n_tc):
    closet = dict()
    n = int(input())
    for idx in range(n):
        name, kind = map(str, input().split())
        if kind in closet:
            closet[kind].append(name)
        else:
            closet[kind] = [name]
    sol(closet)
