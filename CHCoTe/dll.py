#DLL 성공
#Doubly Linked List
class Node:
    def __init__(self,data):
        self.element = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def error_check_add(self,pos):
        cnt = 0
        cur = dll.head
        while cur != self.tail:
            cur = cur.next
            cnt+=1
        return pos <= 0 or pos > cnt

    def add(self, pos, data):
        node = Node(data)
        ptr = self.head
        for i in range(1,pos):
            ptr = ptr.next
        node.next = ptr.next
        node.prev = ptr
        ptr.next.prev = node
        ptr.next = node
        

    def print(self):
        ptr = self.head.next
        while (ptr.next != None):
            print(ptr.element, end = "")
            ptr = ptr.next
        del ptr
        print()

    def error_check(self,pos):
        ptr = self.head.next
        cnt = 0
        while (ptr != self.tail):
            ptr = ptr.next
            cnt +=1
        del ptr
        return (pos <=0 or pos > cnt)

    def delete(self,pos):
        ptr = self.head
        for i in range(pos):
            ptr = ptr.next
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        del ptr

    def get(self,pos):
        ptr = self.head
        for i in range(pos):
            ptr = ptr.next
        print(ptr.element)
        return ptr.element
        
    

dll = DLL()
n = int(input())
for _ in range(n):
    orders = input().split()
    order = orders[0]
    if order == 'A':
        pos = int(orders[1])
        data = orders[2]
        if dll.error_check_add(pos):
            print("invalid position\n")
        else:
            dll.add(pos,data)
    if order == 'P':
        dll.print()
    if order == 'D':
        pos = int(orders[1])
        if dll.error_check(pos):
            print("invalid position\n")
        else:
            dll.delete(pos)
    if order == 'G':
        pos = int(orders[1])
        if dll.error_check(pos):
            print("invalid position\n")
        else:
            elem = dll.get(pos)
