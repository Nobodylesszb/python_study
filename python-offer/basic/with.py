# with as 的用法
"""
创建一个上下文管理类型的时候，就需要实现__enter__
and __exit__方法，

"""
with open('test.txt',mode='w',encoding='utf-8') as f:
    f.write('hello world')