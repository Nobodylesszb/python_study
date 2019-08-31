# 很多程序员并不知道可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代。比如：
class Countdown:
    def __init__(self,start):
        self.start =start

    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n -=1

    def __reversed__(self):
        n = 1
        while n <self.start:
            yield n
            n +=1

for rr in reversed(Countdown(30)):
    print(rr)