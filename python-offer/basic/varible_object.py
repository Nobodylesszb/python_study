# 对可变对象进行测试

a = 10
b = 20
c = [a]
d = c
a = 15
print(c)
c = [10,20]
print(d)
print(id(c),id(d))