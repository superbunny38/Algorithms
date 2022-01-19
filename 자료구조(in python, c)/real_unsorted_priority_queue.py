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
    
class PositionalList(_DoublyLinkedBase):

    """A sequential container of elements allowing positional access."""

    #----------nested Position class-----------
    class Position:
        """An abstraction representing **the location** of a single element."""
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):#equal
            """Return True if other is a Position representing the same position."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):#not equal
            """Return True if other does not represent the same location"""
            return not(self == other)

    #----------utility method------------
    def _validate(self,p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node(or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #---------accessors------------------
    def first(self):
        """Return the first Position in the list(or None if list is empty.)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list(or None if list is empty.)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p(or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()#returns generator
            cursor = self.after(cursor)

    #----------mutators------------------
    #override inherited version to return Position rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self,e):
        """Insert element e at the front of the list, and return new Position."""
        return self._insert_between(e,self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list, and return new position"""
        return self._insert_between(e,self._trailer._prev, self._trailer)

    def add_before(self,p,e):
        """Insert element e into list before position p and return new position"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p,e):
        """Insert element e into list after position p and return new position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at position p."""
        original = self._validate(p)
        return self._delete_node(original)#inherited method returns element

    def replace(self,p,e):
        """Replace the element at position p with e.
        Return the element formerly at Position p."""
        original = self._validate(p)
        old_value = original._element#temporarily store old element
        original._element = e
        return old_value#return the old element value

    def traverse(self):
        print("\n========================List============================")
        cur = self.first()
        while cur is not None:
            print(" |{}|".format(cur.element()._value), end = "")
            cur = self.after(cur)
        print("\n=======================================================\n")
    

class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
            
        def __It__(self, other):
            return self._key < other._key 
        #compare items based on their keys
        
    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element()._key < small.element()._key:
                small = walk
            walk = self._data.after(walk)
        return small
    
    def __init__(self):
        self._data = PositionalList()
    #create a new empty Priority Queue
    
    def size(self):
        return len(self._data)
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.add_last(self._Item(key, value))
        
    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return(item._key, item._value)

    def traverse(self):
        print(">>traverse in order of priority")
        in_order = {}
        for i in range(len(self._data)):
            if self.is_empty():
                raise Empty("Priority queue is empty")
            small = self._data.first()
            walk = self._data.after(small)
            while walk is not None:
                if walk.element()._key < small.element()._key:
                    if walk.element()._key not in in_order:
                        small = walk
                walk = self._data.after(walk)
            print("key:",small.element()._key,"value:",small.element()._value)
            in_order[small.element()._key] = small.element()._value
        print("\n\n in order:")
        return in_order

    def unsorted_traverse(self):
        print(">>traversing list in order of insertion")
        self._data.traverse()
        

UP = UnsortedPriorityQueue()
UP.add(1,'A')
UP.add(3,'C')
UP.add(2,'B')
UP.add(-100,'D')
UP.add(999,'J')
UP.unsorted_traverse()
print(UP.traverse())
print("find_min:",UP._find_min().element()._value)
print("\n\nremoving every data in order of priority")
for i in range(UP.size()):
    print(UP.remove_min())

UP.unsorted_traverse()
