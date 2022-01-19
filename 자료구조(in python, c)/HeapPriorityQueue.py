class HeapPriorityQueue(PriorityQueueBase):#base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""
    #-----------------non public behaviors---------------------------
    def _parent(self,j):
        return (j-1)//2

    def _left(self,j):
        return 2*j+1

    def _right(self,j)
