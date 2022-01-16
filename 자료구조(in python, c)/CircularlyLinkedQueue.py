class Empty(Exception):
    pass

class CircularQueue:
    """queue implementation using circularly linked list for storage"""
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        
        __slots__ = "_element","_next"

        def __init__(self, element, next):# initialize node’s fields
            self._element = element# reference to user’s element
            self._next = next# reference to next node

    def __init__(self):
        """Create an empty queue."""
        self._tail = None# will represent tail of queue
        self._size = 0# number of queue elements

    def len (self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):#get the element next of tail
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")

        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None#empty the queue
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e,None)
        if self.is_empty():#if queue is empty
            newest._next = newest#initialize circularly
        else:
            newest._next = self._tail._next#connect to head
            self._tail._next = newest#old tail points to new node
        self._tail = newest#new node becomes the tail
        self._size +=1

    def rotate(self):
        print("\n====rotate=====")
        """Rotate front element to the back of the queue"""
        if self._size >0:
            self._tail = self._tail._next
        
    def traverse(self):
        print("\n-----display circularly linked queue----")
        cur = self._tail._next#from head
        for i in range(self._size):
            print(cur._element, end = " ")
            cur = cur._next
        print("\n")
        
CQ = CircularQueue()
for j in range(10):
    CQ.enqueue(j+1)
CQ.traverse()
print("dequeued:",CQ.dequeue())
CQ.traverse()
print("dequeued:",CQ.dequeue())
CQ.traverse()
print("first:",CQ.first())
CQ.rotate()
CQ.traverse()
