priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0
    
def postfix_calculator(postfix):
    s = Stack()

    for i in postfix:
        if i in priority:                             
            num1 = s.pop()                              
            num2 = s.pop()
            if i == '+':                                   
                s.push(num2 + num1)
            elif i == '-':                                  
                s.push(num2 - num1)
            elif i == '/':                                  
                s.push(num2 // num1)
            elif i == '*':                                  
                s.push(num2 * num1)                         

        else:                                           
            s.push(int(i))                            

    return s.pop()                                          

N = int(input())
answer = []
for _ in range(N):
    op = input()
    ans = postfix_calculator(op)
    answer.append(ans)

for an in answer:
    print(an)
