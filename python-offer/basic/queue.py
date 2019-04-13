class  Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

    def peek(self):
        if len(self.items):
            return self.items[0]
        else:
            return 'Quene is empty'

    def length(self):
        return len(self.items)

 # 使用两个堆栈实现队列       
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


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push([34,25])
    q.push(78)

    


