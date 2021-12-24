#1506
'''
5
1 2 3 4 5
00011
10000
00010
00100
01000'''
is_connected = []
stack = []
n = int(input())
cost = list(map(int,input().split()))

L=[]
adjacent = []

for i in range(n):
    L.append(list(map(int,list(input()))))

for i in range(n):
    tmp = []
    for j in range(n):
        if L[i][j] == 1:
            tmp.append(j+1)
    adjacent.append(tmp)

print(adjacent)
r = 0
while True:
    start = i + 1
    for j in range(len(adjacent[i]))):
        stack.append(adjacent[i][j])
    goto = stack.pop()
    popped.append(goto)
    for o in range(adjacent[goto-1]):
        stack.append(adjacent[goto-1][o])
    goto = stack.pop()
    popped.append(goto)
        
        
        
