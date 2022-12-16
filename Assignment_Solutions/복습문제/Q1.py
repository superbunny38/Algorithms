# Type or paste your code in this area
class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation"""
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = "_element", "_prev", "_next"#streamline memory
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)#element, prev, next
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer#trailer is after header
        self._trailer._prev = self._header#header is before trailer
        self._size = 0#number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two exiting nodes and return new node."""
        newest = self._Node(e, predecessor,successor)#link to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def insert_node(self, element, position):
        if self._size == 0:
            if int(position) == 1:
                self._insert_between(element,self._header,self._trailer)
            else:
                print("invalid position")
            return
        
        cur = self._header
        if type(position) != int:#manage type
            position = int(position)
        if position > self._size+1:
            print("invalid position")
            return
        for _ in range(position-1):#find position
            cur = cur._next
        predecessor = cur
        successor = cur._next
        newest = self._insert_between(element, predecessor, successor)
        return newest
        
        
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None#deprecate node
        return element#return element of the deleted node

    def delete_node(self, pos):
        if type(pos) != int:#manage type
            pos = int(pos)
        if pos > self._size:
            print("invalid position")
            return
        cur = self._header
        for _ in range(pos):
            cur = cur._next
        self._delete_node(cur)

    def get_entry(self, pos):
        if type(pos) != int:#manage type
            pos = int(pos)
        if pos > self._size:
            print("invalid position")
            return
        cur = self._header
        for _ in range(pos):
            cur = cur._next
        print(cur._element)
    
    def header(self):
        return self._header

    def trailer(self):
        return self._trailer
    
    def traverse(self):
        h = self._header
        print("header ->", end = " ")
        cur = h._next
        for i in range(self._size):
            print("|",cur._element,"|", end = "")
            try:
                cur = cur._next
            except:
                pass
        print("-> trailer")
        
    def print(self):
        h = self._header
        cur = h._next
        for i in range(self._size):
            if i != self._size-1:
                print(cur._element, end = "")
            else:
                print(cur._element)
            try:
                cur = cur._next
            except:
                pass
        
    

DList = _DoublyLinkedBase()
N = int(input())
for _ in range(N):
    tmp_list = [item for item in input().split()]
    op = tmp_list[0]
    if op == 'A':
        pos = tmp_list[1]
        elem = tmp_list[-1]
        DList.insert_node(elem, pos)
    elif op == 'P':
        DList.print()
    elif op == 'D':
        pos = tmp_list[-1]
        DList.delete_node(pos)
    elif op == 'G':
        pos = tmp_list[-1]
        DList.get_entry(pos)
        
        
        
    

'''
first_elem = DList._insert_between(1,DList.header(),DList.trailer())
second_elem = DList._insert_between(2,first_elem,DList.trailer())
third_elem = DList._insert_between(4,second_elem,DList.trailer())
DList.traverse()
deleted = DList._delete_node(second_elem)
print("deleted:",deleted)
DList.traverse()
'''
