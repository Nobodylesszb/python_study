# 生成器版本

# def fib(num):
#     a,b = 0,1
#     for i in range(num):
#         yield b
#         a ,b = b,a + b

# 迭代器版本

def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1)+fib(num-2)
    

print(fib(5))
