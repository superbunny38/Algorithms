# Circular Queue implementation in Python


class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
        self.size = 0

    # Insert an element into the circular queue
    def enqueue(self, data):
        if self.head - self.tail== 1:
            print("overflow",end = "")
            self.exoj_print()
            return False
            
        if ((self.tail + 1) % self.k) == self.head:
            #print("The circular queue is full\n")
            print("overflow",end = "")
            self.exoj_print()
            return False

        elif self.size == self.k-1:
            print("overflow",end = "")
            self.exoj_print()
            return False

        elif (self.head == -1):
            self.head = 1
            self.tail = 1
            self.queue[self.tail] = data
            self.size +=1
            return True
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            self.size +=1
            return True

    # Delete an element from the circular queue
    def dequeue(self):
        if self.head == self.tail:
            print("underflow",end = "")
            return False
        if (self.head == -1):
            print("underflow", end = "")
            return False
        elif self.size == 0:
            print("underflow", end = "")#end = ""해줘야하나?
            return False
        
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.queue[self.head] = None
            self.head = -1
            self.tail = -1
            self.size -=1
            return temp
        else:
            temp = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.k
            self.size-=1
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")
            return False

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
            
    def exoj_print(self):
        for idx,val in enumerate(self.queue):
            if val == None:
                print_val = 0
            else:
                print_val = val
            if idx == self.k -1:
                print(f" {print_val}")
            else:
                print(f" {print_val}",end = "")


q = int(input())
CQ = MyCircularQueue(q)
n = int(input())

for _ in range(n):
    orders = input().split()
    order = orders[0]
    if order == 'I':
        item = orders[1]
        if CQ.enqueue(item):
            continue
        else:
            break
    elif order == "P":
        CQ.exoj_print()
    elif order == 'D':
        d = CQ.dequeue()
        if d:
            continue
        else:
            break
        

