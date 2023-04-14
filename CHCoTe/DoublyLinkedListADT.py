class Node:
    def __init__(self,item):
        self.data = item
        self.prev = None
        self.next =None
        
class DoublyLinkedList:
    def __init__(self):
        self.n_data = 0
        self.head_flag = Node(None)

    def check_valid_pos(self,position):
        if position <=0:
            return False
        elif (position- self.n_data) > 1:
            return False
        return True

    def insert(self, position,item):
        if self.check_valid_pos(position) == False:
            print("invalid position")
            return
        new_node = Node(item)
        if self.n_data == 0:
            self.head_flag.next = new_node
            new_node.prev = self.head_flag
            self.n_data =1
        else:
            cur_node = self.head_flag
            for i in range(position-1):
                cur_node = cur_node.next
            
            if cur_node.next:
                new_node.next = cur_node.next
                new_node.prev = cur_node
                cur_node.next = new_node
                self.n_data +=1
                
            else:
                cur_node.next = new_node
                new_node.prev = cur_node
                self.n_data +=1
                
    def get(self,position):
        if self.check_valid_pos(position) == False:
            print("invalid position")
            return
        if position > self.n_data:
            print("invalid position")
            return
        cur_node = self.head_flag
        for i in range(position):
            cur_node = cur_node.next
        print(cur_node.data)

    def print(self):
        cur_node = self.head_flag
        for i in range(self.n_data):
            if i != self.n_data -1:
                cur_node = cur_node.next
                print(cur_node.data,end = "")
            else:
                cur_node = cur_node.next
                print(cur_node.data)

    def delete(self, position):
        if self.check_valid_pos(position) == False:
            print("invalid position")
            return
        if position > self.n_data:
            print("invalid position")
            return
        if position == self.n_data:#마지막 삭제
            cur_node = self.head_flag
            for i in range(self.n_data-1):
                cur_node = cur_node.next
            #print(cur_node.next.data)
            cur_node.next = None
            self.n_data -=1
        elif position == 1:
            self.n_data -=1
            delete_node = self.head_flag.next
            self.head_flag.next = delete_node.next
            delete_node.next.prev = self.head_flag
            #print(delete_node.data)
            del delete_node
            
        else:
            cur_node = self.head_flag
            for i in range(self.n_data-2):
                cur_node = cur_node.next
            delete_node = cur_node.next
            #print(delete_node.data)
            cur_node.next = delete_node.next
            delete_node.next.prev = cur_node
            self.n_data -=1
            
DLL = DoublyLinkedList()
N = int(input())
for i in range(N):
    command = input().split()
    order = command[0]
    if order == 'A':
        position,item = int(command[1]),command[2]
        DLL.insert(position,item)
    elif order == 'P':
        DLL.print()
    elif order == 'G':
        position = int(command[1])
        DLL.get(position)
    elif order == 'D':
        position = int(command[1])
        DLL.delete(position)
