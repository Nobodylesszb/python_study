class Quantity:
    __count = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__count
        self.storage_name = '_{}#{}'.format(prefix, index)

    def __get__(self, instance, owner):
        """
        这里可以使用内置的高阶函数getattr,和setattr存取值，无需使用
        instance.__dict__，因为托管属性和存储属性不同，所以把存储属性
        传给getattr函数不会触发描述符。
        """
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)

        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

"""
__get__方法有三个参数，self,instance,owner，owner参数是托管类（如Lineitem）的引用，通过描述符
从托管类中获得属性时候用得到，通过描述符从托管类中获得属性时候用得到，如果使用LineItem.weight从类中
获得托管属性，描述符的__get__方法接收的instance参数值是None,
"""
s = LineItem('test', 100, 2)
print(s.price)
