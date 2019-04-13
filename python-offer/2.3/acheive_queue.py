class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'