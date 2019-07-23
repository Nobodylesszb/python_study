class HauntedBus:
    def __int__(self,passengers = []):
        self.passengers = passengers
    
    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

"""
如果不为HauntBus指定乘客的话，奇怪的事发生了。这是因为self.passengers变成了passengers参数默认值的别名
默认值在定义函数时计算。因此默认值变成函数对象的属性。因此，如果默认值为可变对象
而且修改了它的值。那么后续的函数调用都会受到影响
"""



