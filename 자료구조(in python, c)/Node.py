class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'#streamline memory usage

    def __init__(self, element, next):#initialize node's fields
        self._element = element#reference to user's element
        self._next = next#reference to next node
        
