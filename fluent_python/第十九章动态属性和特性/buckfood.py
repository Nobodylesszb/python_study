class LineItem:
    def __init__(self, desciption, weight, price):
        self.desciption = desciption
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight  # 真正的值存储在私有变量__weight中

    @weight.setter  # 被装饰的读值有一个。setter属性。这个属性也是装饰器。可以把读值方法和设值方法联系在一起
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be >0')

    
walnut = LineItem('walnut',0,10)
"""
ValueError: value must be >0
"""

