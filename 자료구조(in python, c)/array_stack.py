class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    def __init__(self):
        """create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_empty(self):
        """return true if stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """add element e to the top of the stack."""
        return self._data.append(e)

    def top(self):
        """
        return (but do not remove) the element at the top of the stack.
        raise empty function if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack
        Raise Empty excepption if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
    
        
