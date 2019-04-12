
# list_a = []
# def a():
#     list_a = [1]      ## 语句1
# a()
# print (list_a)    # []


# list_b = []
# def b():
#     list_b.append(1)    ## 语句2
# b()
# print (list_b)    # [1]


"""
[]
[1]
为什么 语句1 不能改变 list_a 的值，而 语句2 却可以？他们的差别在哪呢
因为 = 创建了局部变量，而 .append() 或者 .extend() 重用了全局变量。
"""

# a = [1]
# b = a
# print (id(a),id(b))
# a.append(3)
# print('a:{a},b:{b}'.format(a=a,b=b))


a = 'test'
b = a
print (id(a),id(b))
# a = a + '1'
a += '1'
print('a:{a},b:{b}'.format(a=a,b=b))
print (id(a),id(b))