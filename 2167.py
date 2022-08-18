#2167
#Chaeeun Ryu

def get_sum(i,j,x,y,matrix):
    summ = 0
    for a in range(i,x+1,1):
        for b in range(j,y+1,1):
            summ += matrix[a][b]
    return summ

size = list(map(int,input().strip().split()))
n,m = size[0],size[1]

matrix = []
for _ in range(n):
    a = list(map(int,input().strip().split()))
    matrix.append(a)

results = []
k = int(input())
for _ in range(k):
    i,j,x,y = map(int, input().split())
    result_sum = get_sum(i-1,j-1,x-1,y-1,matrix)
    #print(f"sum: {result_sum}")
    results.append(result_sum)

for r in results:
    print(r)
