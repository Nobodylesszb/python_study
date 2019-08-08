"""
使用特性工厂函数实现描述符相同的功能
"""

def quantity:
    try:
        quantity.count +=1
    except AttributeError:
        quantity.count =0 # 如果quantity不存在，把值设为0
    """
    我们没有实例变量，因此创建一个局部变量storage_name,借助闭包保持他的值
    供后面的quty_getter和qty_setter函数使用
    """
    storage_name = '_{}:{}',format('quantity',quantity.count)

    def qty_getter(instance):
        return getattr(instance,storage_name)

    def qty_setter(instance,value):
        if value >0:
            setattr(instance,storage_name,value)
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter,qty_setter)