from ImportHeapPriorityQueue import *
class AdaptableHeapPriorityQueue(HeapPriorityQueue):

    #-------------nested Locator class----------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locaing an entry of the priority queue."""
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index= j
            
    #------------nonpublic behaviors-----------------
    
    def _swap(self,i,j):
        super()._swap(i,j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self,j):
        if j >0 and self._data[j]._key < self._data[self._parent(j)]._key:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self,key,value):
        """Add a key-value pair"""
        token = self.Locator(key,value,len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self,loc,newkey,newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        if not(0<=j<len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self,loc):
        """Remove and return the (k,v) pair identified by Locator loc."""
        j = loc._index
        if not (0<=j<len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) -1:
            self._data.pop()
        else:
            self._swap(j,len(self)-1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)

    def traverse(self):
        print("traverse")
        if len(self._data) == 0:
            print("empty")
        else:
            for d in self._data:
                print("index:{} key:{} value:{}".format(d._index,d._key,d._value))
            
AH = AdaptableHeapPriorityQueue()
f = AH.add(1,"A")
AH.add(2,"B")
AH.add(0,"C")
h = AH.add(100,"all the good girls go to hell.")
AH.add(-99999,"Chaeeun")
AH.traverse()
print("\nafter removal")
AH.remove(h)
AH.traverse()

print("\nupdate")
AH.update(f,-9,'Chaeeun')
AH.traverse()
