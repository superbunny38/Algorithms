from import_linked_binary_tree import *
#1991

N = int(input())
nodes_list = []
for i in range(N):
    nodes_list.append(list(map(str, input().split())))
'''
for n in nodes_list:
    print(n)#노드, 왼쪽 자식 노드, 오른쪽 자식 노드
'''
LT = LinkedBinaryTree()
for idx,n in enumerate(nodes_list):
    if idx == 0:
        root = n[0]
        rt = LT._add_root(root)
        if n[1] != '.':
            left = n[1]
            LT._add_left(rt,left)
        if n[2] != '.':
            right = n[2]
            LT._add_right(rt,right)
    else:
        node_element = n[0]
        node = LT.find(node_element)
        if n[1] != '.':
            left = n[1]
            LT._add_left(node,left)
        if n[2] != '.':
            right = n[2]
            LT._add_right(node,right)
result = []
for p in LT.preorder():
    result.append(p.element())
print("".join(result))
result = []
for p in LT.inorder():
    result.append(p.element())
print("".join(result))
result = []
for p in LT.postorder():
    result.append(p.element())
print("".join(result))
