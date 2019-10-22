def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    p_arg = ','.join(display(x)for x in args)
    print('->{}.__{}__{}').format(cls_name(args[0]), name, p_arg)


class Overriding:
    """
    数据描述符
    """

    def __get__(self, instance, owner):
        print_args('get', self,instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """
    覆盖型描述符
    """
    def __set__(self,instance,value):
        print_args('set', self, instance, value)


class NonOverriding:
    """
    非数据行描述符
    """
    def __get__(self, instance, owner):
        print_args('get', self,instance, owner)

class Managed:
    over = Overriding()
    over_not_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> managed.spam({})'.format(display(self)))