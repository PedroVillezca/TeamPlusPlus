class Stack:
    """
    Standard definition of a Stack class. Defined because Python doesn't support
    this structure natively. 
    """

    def __init__(self):
        self.elements = []
    
    def push(self, item):
        self.elements.append(item)
    
    def pop(self):
        return self.elements.pop()
    
    def empty(self):
        return not self.elements
    
    def size(self):
        return len(self.elements)
    
    def top(self):
        return self.elements[-1]

    def __repr__(self):
        return f"{self.elements}"


class Queue:
    """
    Standard definition of a Queue class. Defined because Python doesn't support
    this structure natively. 
    """

    def __init__(self):
        self.elements = []
    
    def push(self, item):
        self.elements.append(item)
    
    def pop(self):
        return self.elements.pop(0)
    
    def empty(self):
        return not self.elements
    
    def size(self):
        return len(self.elements)
    
    def front(self):
        return self.elements[0]

    def at(self, i):
        return self.elements[i]

    def replace(self, i, item):
        self.elements[i] = item

    def __repr__(self):
        return f"{self.elements}"