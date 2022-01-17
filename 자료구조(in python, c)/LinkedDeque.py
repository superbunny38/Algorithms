class Empty(Exception):
    pass

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
        self._insert_between(e,self._header,self._header._next)

    def insert_last(self,e):
        """Add an element to the back of the deque."""
        self._insert_between(e,self._trailer._prev, self._trailer)

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

    def traverse(self):
        print("\n-----Deque------")
        h = self._header
        c = h._next
        for i in range(self._size):
            print("|",c._element,"|", end = "")
            c = c._next
        print("\n----------------\n")
            
DQ = LinkedDeque()
DQ.insert_first("2")
DQ.insert_first("1")
DQ.insert_last("3")
DQ.traverse()
print(">>first element",DQ.first())
print(">>last element",DQ.last())
d = DQ.delete_last()
print(">>Delete last element:",d)
DQ.traverse()
d = DQ.delete_first()
print(">>Delete first element",d)
DQ.traverse()
