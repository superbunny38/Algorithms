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
    
DList = _DoublyLinkedBase()
first_elem = DList._insert_between(1,DList.header(),DList.trailer())
second_elem = DList._insert_between(2,first_elem,DList.trailer())
third_elem = DList._insert_between(4,second_elem,DList.trailer())
DList.traverse()
deleted = DList._delete_node(second_elem)
print("deleted:",deleted)
DList.traverse()
