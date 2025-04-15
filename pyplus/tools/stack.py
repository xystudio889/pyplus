class FIFOStack:
    def __init__(self):
        self.stacks = []

    def push(self, items):
        self.stacks.append(items)

    def put(self):
        return self.stacks.pop(0)
    
    @property
    def is_empty(self):
        return len(self.stacks) == 0
    
    def __sizeof__(self):
        return len(self)
        
    def __len__(self):
        return len(self.stacks)
    
    def __repr__(self):
        return f"Stack({",".join(self.stacks)})"
    
    def  __str__(self):
        return self.__repr__()
    
    def __add__(self, value):
        out_list = self.stacks.append(value)
        o = FIFOStack()
        o.stacks = out_list
        return o
    
    def __mul__(self, value):
        return [self, self, self]

class LIFOStack:
    pass
