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
    def find(self,e):
        cur = self.first()
        while cur is not None:
            cur = self.after(cur)
            if cur.element() == e:
                return cur

    def traverse(self):
        print("\n========================List============================")
        cur = self.first()
        while cur is not None:
            print(" |{}|".format(cur.element()), end = "")
            cur = self.after(cur)
        print("\n=======================================================\n")
'''
PL = PositionalList()
#add elements to list
PL.add_first(1)
for i in range(9):
   PL.add_last(i+2)
PL.traverse()
print("first position in list:",PL.first().element())
h = PL.add_first("h")
o = PL.add_first("o")
p = PL.add_first("p")
PL.traverse()
print("first position in list:",PL.first().element())

d = PL.delete(o)
print("Delete:",d)
PL.traverse()

PL.replace(h,"i")
print("replace h with i ")
PL.traverse()
'''
