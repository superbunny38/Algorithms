# Type or paste your code in this area
#[문제2] 상향식 힙 생성
# 2018312824
# 류채은

#왜지?

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
    
    def downHeap(self,v):#그대로 사용
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

    def print(self):#그대로 사용
        for idx, d in enumerate(self.data):
            if d == None:
                continue
            if idx != len(self.data)-1:
                print(f" {d}", end = "")
            else:
                print(f" {d}")
            
        return

    def insertRoot(self, k):
        self.data.insert(1,k)
        self.size +=1
        self.last +=1
        return
    
    def rBuildHeap(self,idx):
        n = self.size
        if idx <= n:
            if idx*2 <= n:
                self.rBuildHeap(idx*2)
            if (idx*2+1)<=n:
                self.rBuildHeap(idx*2+1)
        self.downHeap(self.data[idx])

def printHeap(data):
    for idx, d in enumerate(data):
        if d == None:
            continue
        if idx != len(data)-1:
            print(f" {d}", end = "")
        else:
            print(f" {d}")
    
def recursiveBuildHeap(L):#상향식 힙 생성 재귀 버전 알고리즘
    print("L:",L)
    if len(L) == 1 or len(L) == 0:#empty
        return [None]
    k = L.pop(1)
    mid = int((len(L)+1)//2)
    L1 = L[:mid]
    L2 = [None]+L[mid:]
    T1 = recursiveBuildHeap(L1)
    T2 = recursiveBuildHeap(L2)
    T = Heap()
    T.insertRoot(k)
    level = 0
    if T1[0] == None:
        T1.pop(0)
    if T2[0] == None:
        T2.pop(0)
    print(f"merging... root: {k}, T1:{T1},T2:{T2}")
    while True:
        print("level:",level)
        num_nodes = 2**level
        if len(T1) == 0 and len(T2) == 0:
            break
        for _ in range(num_nodes):
            try:
                node_1 = T1.pop(0)
                if node_1 != None:
                    T.data.append(node_1)
                    T.size +=1
                    T.last +=1
            except:
                break
        for _ in range(num_nodes):
            try:
                node_2 = T2.pop(0)
                if node_2 != None:
                    T.data.append(node_2)
                    T.size +=1
                    T.last +=1
            except:
                break
        level += 1
    
    T.downHeap(T.root())
    print("tree built: ", T.data)
    return T.data

n = int(input())
heap = Heap()
inputs = input().split()
inputs = [int(x) for x in inputs]
heap.size += len(inputs)
heap.last += len(inputs)
inputs = [None] + inputs
heap.data = inputs
heap.rBuildHeap(1)
#print("inputs:",inputs)
sorted_L = heap.data

printHeap(sorted_L)
