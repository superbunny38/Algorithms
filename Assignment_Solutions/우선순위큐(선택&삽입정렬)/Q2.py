#Q2
#2018312824
#Chaeeun Ryu

N = int(input())
L = [int(item) for item in input().split()]
for pass_ in range(1,N,1):
    save = L[pass_]
    j = pass_-1
    while j >= 0 and L[j] > save:
        L[j+1] = L[j]
        j = j -1
    L[j+1] = save

for elem in L:
    print(f" {elem}", end = "")
# Type or paste your code in this area
