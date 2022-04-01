class Empty(Exception):
    pass

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    
    class _Node:
        """Lightewight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element","_next"

        def __init__(self, element, next):# initialize node’s fields
            self._element = element# reference to user’s element
            self._next = next# reference to next node
    
    def __init__(self):
        """Create an empty stack."""
        self._head = None# reference to the head node
        self._size = 0# number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        #print("push:{}".format(e))
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)#create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is Empty")#error message
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        #print("popped:{}".format(answer))
        return answer
    def size(self):
        return self._size

def split(word):
    return [char for char in word]

def check_valid_VPS(stack):
    remaining_stack = []
    
    for i in range(stack.size()):
        try:
            bracket = stack.pop()
            #print("popped:",bracket)
        except:
            print("stack empty")
            return "NO"
        if len(remaining_stack) == 0:
            remaining_stack.append(bracket)
        else:
            peek = remaining_stack[-1]
            if peek == ')' and bracket == '(':
                remaining_stack.pop()
            else:
                remaining_stack.append(bracket)
                
    
    if len(remaining_stack) == 0:
        return "YES"
    else:
        return "NO"
    

T = int(input())
received = []
for _ in range(T):
    strings = input()
    received.append(split(strings))



for r in received:
    LS = LinkedStack()
    for l in r:
        LS.push(l)
    print(check_valid_VPS(LS))
        

"""

for idx,stack in enumerate(strings_stack):
    #print("\n\n {}".format(idx))
    #print("".join(stack))
    print(check_valid_VPS(stack))
"""
