class MinStack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        if not self.stack:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(x,self.stack[-1][1])))
    
    def top(self):
        if self.stack:
            self.stack.pop()
        else:
            return None
    
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None
    
        