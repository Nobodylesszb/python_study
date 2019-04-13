# class stack(object):
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return len(self.items) == 0
#     def push(self,item):
#         return self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def lenth(self):
#         return len(self.items)
#     def peek(self):
#         return self.items[len(self.items)-1]

class stack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def isEmpty(self):
        return len(self.stack2) == 0 
      #每次进栈都往1中添加
    def push(self,item):
        return self.stack1.append(item)
     #每次出栈先把1中加到2中，从2中出
    def pop(self):
        if len(self.stack1) >= 1:
            self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return 'stack is empty'
    def length(self):
        return len(self.stack1) + len(self.stack2)


if __name__ == "__main__":
    s= stack()
    s.push(1)
    s.push(3)
    s.push([123,456])

    
