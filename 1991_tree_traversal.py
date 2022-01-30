from import_linked_binary_tree import *
#1991
N = int(input())
nodes_list = []
for i in range(N):
    nodes_list.append(list(map(int, input().split())))

for n in nodes_list:
    print(n)
