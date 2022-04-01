from import_linked_binary_tree import *


N = int(input())
parents_list = list(map(str, input().split()))
R = int(input())

LT = LinkedBinaryTree()

node_names = []
for _ in range(N):
    node_names.append('A'+str(_))

for idx,p in enumerate(parents_list):
    if p == '-1':
        LT._add_root('A0')
    else:
        parent_name = 'A'+str(p)
        parent = LT.find(parent_name)
        LT._add(parent,'A'+str(idx))
    

remove = LT.find('A'+str(R))

LT.destroy(remove)
'''
for p in LT.dfs():
    print(p.element())
#print("\n\nbf\n")
for p in LT.breadthfirst():
    print(p.element())
print("\n\n")
'''
count = 0
for p in LT.dfs():
    if LT.num_children(p) == 0:
        
        count += 1
print(count)
