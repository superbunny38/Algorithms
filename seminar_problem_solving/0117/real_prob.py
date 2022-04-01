class Empty(Exception):
    pass
def split(word):
    return [char for char in word]

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
    
class LinkedDeque(_DoublyLinkedBase):#use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""
    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element #real item just after the header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add adn element to the front of the deque."""
        return self._insert_between(e,self._header,self._header._next)

    def insert_last(self,e):
        """Add an element to the back of the deque."""
        return self._insert_between(e,self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the queue."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)

    def is_last_node(self,node):
        if node._next == self._trailer:
            return True
        else:
            return False
        
    def is_first_node(self,node):
        if node._prev == self._header:
            return True
        else:
            return False
    def is_header(self,cur):
        if self._header == cur:
            return True
        else:
            return False

    def traverse(self,cur):
        print("\n-----Deque------")
        h = self._header
        c = h._next
        for i in range(self._size):
            print("|",c._element,"|", end = "")
            c = c._next
        print("\n----------------\n")
        print("cursor at:",cur._element)
    def return_password(self):
        h = self._header
        c = h._next
        for i in range(self._size):
            print(c._element,end = "")
            c = c._next
    def update_password(self,r):
        h = self._header
        for order in r:
            #print("\n\n\n>>order:",order)
            if self._size == 0:
                if order == '<' or order == '>' or order == '-':
                    #print("pass")
                    continue
                else:
                    first_elem = self.insert_first(order)
                    cur = first_elem
            else:
                if order == '<':
                    if self.is_header(cur) == False:
                        cur = cur._prev
                elif order == '>':
                    if self.is_last_node(cur) == False:
                        cur = cur._next
                elif order == '-':
                    if self.is_first_node(cur) == True:
                        self.delete_first()
                        cur = self._header
                    elif self.is_header(cur) == True:
                        pass
                    else:
                        move_to = cur._prev
                        self._delete_node(cur)
                        cur = move_to
                else:
                    cur = self._insert_between(order,cur,cur._next)
            #self.traverse(cur)
        self.return_password()
                
            
T = int(input())
received = []
for _ in range(T):
    strings = input()
    received.append(split(strings))


for r in received:
    DQ = LinkedDeque()
    DQ.update_password(r)
    print("\n")
            
