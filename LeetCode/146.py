class Node:
    def __init__(self,key,val,next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    
    def __init__(self, capacity):
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = capacity
        print('NULL')

    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        return 
    
    def insert(self, node):
        mru = self.right.prev
        mru.next = node
        node.prev = mru
        self.right.prev = node
        node.next = self.right
        return

    def get(self, key):
        ret = -1
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(Node(key=key,val=val))
            return val
        return ret
    
    def put(self, key, value):
        insert_node = Node(key=key,val=value)
        self.insert(insert_node)
        self.cache[key] = insert_node
        
        if len(self.cache)>self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        return 'NULL'

obj = LRUCache(2)
print(obj.put(2,1))
print(obj.cache.keys())
print(obj.put(1,1))
print(obj.cache.keys())
print(obj.put(2,3))
print(obj.cache.keys())
print(obj.put(4, 1))
print(obj.cache.keys())
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

# obj = LRUCache(1)
# print(obj.put(2,1))
# print(obj.cache.keys())
# print(obj.get(2))
