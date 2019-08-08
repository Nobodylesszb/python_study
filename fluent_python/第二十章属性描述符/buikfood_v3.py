class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            # 这里，必须直接处理托管实例的__dict__属性，如果使用内置的setattr函数，会再次触发set,无线循环
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be >0')

"""
编写__set__方法时候，要记住self 和instance 参数的意思：self是描述符实例，instance是托管实例
管理实例属性的描述符应该把值储存在托管实例中，因此，python才在描述符中的那个方法提供instance参数
"""
class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, decription, weight, price):x
        self.decription = decription
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price



t = LineItem('white',100,8)
print(t.weight)
"""
100
"""