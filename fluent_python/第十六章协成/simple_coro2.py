def simple_coro(a):
    print('start a = ', a)
    b = yield a
    print('received b = ',b)
    c = yield a +b
    print('receive c =', c)

"""
my = simple_coro(14)
next(my) 初始化
打印第一个消息。然后执行yield a 产出数字14
my.send(28) 发送 
把28 赋值与b,打印第二个消息。然后执行yiald a+b
my.send(99),将99赋值与c

"""