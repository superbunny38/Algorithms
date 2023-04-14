class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node= None
        self.n_data = 0

    def check_valid_position(self,position):
        if position > self.n_data+1:
            return False
        if position <= 0:
            return False
        return True

    def insert(self,position,item):
        if self.check_valid_position(position) == False:
            print("invalid position")
            return
        
        if self.n_data == 0:
            new_node = Node(item)
            self.start_node = new_node
            self.n_data +=1
            return
        
        cur_node = self.start_node
        new_node = Node(item)
        
        for pos in range(position-2):
            cur_node = cur_node.next
            
        if cur_node.next == None:#마지막 노드임
            cur_node.next = new_node
            new_node.prev = cur_node
            self.n_data +=1
            return
        else:
            new_node.next= cur_node.next
            new_node.prev = cur_node
            cur_node.next = new_node
            self.n_data +=1
            return
        
    def delete(self,position):
        if self.check_valid_position(position) == False:
            print("invalid position")
            return
        if position == 1:#맨 앞 지움
            next_node = self.start_node.next
            self.start_node.next = None
            self.start_node = next_node
            self.n_data -=1
        else:
            cur_node = self.start_node
            for pos in range(position-2):
                cur_node = cur_node.next
            #cur_node = prev_node of node to delete
            del_node = cur_node.next
            cur_node.next = del_node.next
            del_node.next.prev = cur_node
            del_node.prev = None
            del_node.next = None
            self.n_data -=1
            return
        
        
    def print(self):
        print("current data")
        cur_node = self.start_node
        for i in range(self.n_data):
            if i != self.n_data -1:
                print(cur_node.data, end = " ")
                cur_node = cur_node.next
            else:
                print(cur_node.data)
                cur_node = cur_node.next

N = int(input())

DLL = DoublyLinkedList()

for _ in range(N):
    order_str = input().split()#list type
    letter = order_str[0]
    if letter == 'A':
        position,item = int(order_str[1]),order_str[2]
        DLL.insert(position,item)

    elif letter == 'D':
        position = int(order_str[1])
        DLL.delete(position)
        
    elif letter == 'P':
        DLL.print()
        
