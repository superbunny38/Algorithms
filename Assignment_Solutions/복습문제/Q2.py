class LinkedBinaryTree:
    def __init__(self):
        self._size = 0
        self._root = None
        
    class Node:
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    def add_root(self, e):
        self._size = 1
        self._root = self.Node(e)
        return self._root

    def add_right(self, to, e):#to = node, e = element
        self._size +=1
        node_e = self.Node(e, to)
        to._right = node_e
        return

    def add_left(self, to, e):
        self._size +=1
        node_e = self.Node(e, to)#parent = to
        to._left = node_e
        return

    def display_preorder(self):
        print("=======tree=======\n")
        current = self._root
        stack = []
        while current is not None or len(stack):
            while current is not None:
                if current._element != 0:
                    print(current._element, end = " ")
                if current._right is not None:
                    stack.append(current._right)
                current = current._left
            if (len(stack)> 0):
                current = stack[-1]
                stack.pop()
        print("\n==================")
        
    def traverse_preorder_and_find_key_and_add_childeren(self, key, left, right):
        current = self._root
        stack = []
        while current is not None or len(stack):
            while current is not None:
                if current._element == key:
                    self.add_left(current, left)
                    self.add_right(current, right)
                    return
                if current._right is not None:
                    stack.append(current._right)
                current = current._left
            if len(stack)>0:
                current = stack[-1]
                stack.pop()

    def traverse_search(self, search_):
        steps = len(search_)
        cur = self._root
        print(cur._element, end = " ")
        for i in range(steps):
            way = search_[i]
            if way == 'R':
                cur = cur._right
            elif way == 'L':
                cur = cur._left
            if i < steps -1:
                print(cur._element, end = " ")
            else:
                print(cur._element)
        return
    
BinaryTree = LinkedBinaryTree()
n = int(input())
for idx in range(n):
    tmp_ = [int(item) for item in input().split()]
    cur, left, right = tmp_[0], tmp_[1], tmp_[2]
    if idx == 0:
        root = BinaryTree.add_root(cur)
        BinaryTree.add_left(root, left)
        BinaryTree.add_right(root,right)
    else:
        BinaryTree.traverse_preorder_and_find_key_and_add_childeren(cur, left, right)
    #BinaryTree.display_preorder()

n_search = int(input())
for _ in range(n_search):
    search_ = list(input())
    #print(search_)
    BinaryTree.traverse_search(search_)
# Type or paste your code in this area
