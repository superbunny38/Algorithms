# Type or paste your code in this area
class Heap:
    def __init__(self):
        self.data = [None]
        self.last = 0
        self.size = 0
        
    def expandExternal(self, z):
        self.last +=1
        self.size +=1

    def root(self):
        return self.data[1]

    def isRoot(self,v):
        if self.data.index(v) == 1:
            return True
        else:
            return False
        
    def key(self,v):
        return v

    def parent(self, v):
        parent_idx = self.data.index(v)//2
        return self.data[parent_idx]

    def swapElements(self,d1,d2):
        d1_index = self.data.index(d1)
        d2_index = self.data.index(d2)
        self.data[d1_index], self.data[d2_index] = d2,d1
        return self.data[d1_index], self.data[d2_index]
        

    def upHeap(self, v):
        #print("Up heap with",v)
        #self.print()
        if self.isRoot(v) ==  True:
            return
        if self.key(v) <= self.key(self.parent(v)):
            return
        v,_ = self.swapElements(v, self.parent(v))
        self.upHeap(_)
        
        
    def insertItem(self, K):
        self.data.append(K)
        self.expandExternal(K)
        self.upHeap(K)
        return 0

    def reduceExternal(self):
        self.data.pop()
        return

    def leftChild(self,v):
        v_idx = self.data.index(v)
        try:
            return self.data[v_idx*2]
        except:
            return False

    def rightChild(self,v):
        v_idx = self.data.index(v)
        try:
            return self.data[v_idx*2+1]
        except:
            return False
    
    def downHeap(self,v):
        if self.leftChild(v) == False and self.rightChild(v) == False:
            return
        larger = self.leftChild(v)
        if self.rightChild(v) != False:
            larger = max(larger, self.rightChild(v))
        if (v >= larger):
            return
        v,larger =self.swapElements(v,larger)
        self.downHeap(larger)

    def removeMax(self):
        k = self.root()
        w = self.data[-1]
        self.data[1] = w
        self.reduceExternal()
        self.downHeap(self.data[1])
        return k

    def print(self):
        for idx, d in enumerate(self.data):
            if d == None:
                continue
            if idx != len(self.data)-1:
                print(f" {d}", end = "")
            else:
                print(f" {d}")
            
        return

heap = Heap()
while True:
    inputs = input().split()
    order = inputs[0]
    if order == 'q':
        break
    elif order == 'i':
        #heap.print()
        key = int(inputs[1])
        print(heap.insertItem(key))
        #heap.print()
    elif order == 'd':
        print(heap.removeMax())
    elif order == 'p':
        heap.print()
