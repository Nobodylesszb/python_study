class LookingGlass:
    def __enter__(self):  # 1
        import sys
        self.oringin_write = sys.stdout.write  # 2
        sys.stdout.write = self.reaver_write  # 3
        return 'jaaverwo'  # 4

    def reaver_write(self, text):
        self.oringin_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # 6
        import sys

        sys.stdout.write = self.oringin_write  # 8
        if exc_type is ZeroDivisionError:
            print('DO NOT DIVIDE BY ZEAO')
            return True  # 10


if __name__ == '__main__':
    with LookingGlass() as what:
        print('alice,ketty and snow')
        print(what)

"""
1. 除去self之外，python 调用__enter__方法不传入其他
2. 把原来的sys.std.write方法保存在一个实例属性中，供后面使用
3. 为sys,stdout.write打猴子补丁，替换成自己编写的方法
4.返回数据到变量what
8 还原按原来的sys.stdout.write方法
"""
