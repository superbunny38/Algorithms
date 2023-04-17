# 틀려서 다시 짜는 중..
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

    def _valid_pos(self,position):
        if position > self._size+1:
            return False
        if position <= 0:
            return False
        return True
    
    def header(self):
        return self._header

    def trailer(self):
        return self._trailer

    def get_node(self,position):
        if self._valid_pos(position) == False:
            print("invalid position")
            return
        if position > self._size:
            print("invalid position")
            return
        
        h = self._header
        cur = h
        for i in range(position):
            cur = cur._next
        return cur
    
    def traverse(self):
        h = self._header
        #print("header ->", end = " ")
        cur = h._next
        for i in range(self._size):
            if i == self._size -1:
                print(cur_element)
            else:
                print(cur._element, end = " ")
            try:
                cur = cur._next
            except:
                pass
        #print("-> trailer")

    def insert(self,e,position):
        if self._valid_pos(position) == False:
            print("invalid position")
            return
        if self._size == 0:
            self._insert_between(e,self._header,self._trailer)
            return
        h = self._header
        cur = h
        for i in range(position-1):
            cur = cur._next
        next_node = cur._next
        self._insert_between(e,cur,next_node)
        return

    def delete(self,position):
        if self._valid_pos(position) == False:
            print("invalid position")
            return
        if position > self._size:
            print("invalid position")
            return
        
        del_node = self.get_node(position)
        self._delete_node(del_node)
        return
    
DList = _DoublyLinkedBase()

N = int(input())
for _ in range(N):
    orders = input().split()
    command = orders[0]
    if command == 'A':
        position,data = int(orders[1]), orders[2]
        DList.insert(data,position)
        
    elif command == 'P':
        DList.traverse()
        
    elif command == 'G':
        position = int(orders[1])
        ret_node = DList.get_node(position)
        if ret_node:
            print(ret_node.data)
    elif command == 'D':
        position = int(orders[1])
        DList.delete(position)
