# 实现特性工厂函数


def quantity(storage_name):  # storage_name 参数确认各个特性的数据储存在哪里，对weight特性来说，储存的名称为weight
    def qty_getter(instance):
        """
        qty_getter函数的第一个函数可以名为self,但是qty_getter函数不在类定义中，instance
        指代要把属性储存其中的LineItem实例
        """
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] == value
        else:
            raise ValueError('value must be >0')
    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity('weight')  # 使用工厂函数把第一个自定义的特性weight定义类属性
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 这里。特性已经激活，却把不能把weight设为负数
        self.price = price

    def subtotal(self):
        return self.weight * self.price  # 这里也用到特性，使用特性获取实例中存储的值


nutmsg = LineItem('test',8,13)
print(nutmsg.weight,nutmsg.price)