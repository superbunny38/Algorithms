class Empty(Exception):
    """Error attempting to access an Element from an empty container"""
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10#moderate capacity for all new queues

    def __init__(self):
        """create an empty queue"""
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty")#Raise EmptyException if the queue is empty.
        print("first: {}".format(self._data[self._front]))
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue(i.e., FIFO)."""
        if self.is_empty():
            raise Empty('Aueue is empty')#Raise Empty exception if the queue is empty.
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -=1
        print("dequeued: {}".format(answer))
        return answer

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front = 0

    def enqueue(self, e):
        print("enqueue: {}".format(e))
        """Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1

    def displayQ(self):
        print("\nDisplay Queue")
        print("<-front --- back<-")
        print("====================")
        print(self._data)
        print("====================")
    

    
        
Q = ArrayQueue()
for i in range(10):
    Q.enqueue(i+1)
Q.displayQ()
Q.enqueue(11)
Q.displayQ()
Q.dequeue()
Q.dequeue()
Q.displayQ()
