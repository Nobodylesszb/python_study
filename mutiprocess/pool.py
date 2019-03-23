from multiprocessing import Queue, Process, Pool
import time
import os

# def test():
#     time.sleep(2)
#     print('this is process {}'.format(os.getpid()))

# def get_pool(n=5):
#     p = Pool(n) # 设置进程池的大小
#     for i in range(10):
#         p.apply_async(test)
#     p.close() # 关闭进程池
#     p.join()

# if __name__ == '__main__':
#     get_pool()
#     print('ths process is ended')

"""
output:
this is process 9824
this is process 9824
this is process 9336
this is process 9336
this is process 3096
this is process 3096
this is process 976
this is process 976
this is process 5200
this is process 5200
ths process is ended

"""


def test(n):
    time.sleep(1)
    print('this is process {}____'.format(os.getpid()))
    print(n)
    return n

def test1(n, m):
    print('test{n}:{m}'.format(n=n,m=m))
    print('this is process {}------'.format(os.getpid()))

def back_func(values): # 多进程执行完毕会返回所有的结果的列表
    print(values)

def back_func_err(values): # 多进程执行完毕会返回所有错误的列表
    print(values)

def get_pool(n=5):
    p = Pool(n)
    # p.map(test, (i for i in range(10))) # 阻塞式多进程执行
    # p.starmap(test1, zip([1,2,3],[3,4,5])) # 阻塞式多进程执行多参数函数
    # 异步多进程执行函数
    p.map_async(test, (i for i in range(5)), callback=back_func, error_callback=back_func_err)
    # 异步多进程执行多参数函数
    p.starmap_async(test1, zip([1,2,3],[3,4,5]), callback=back_func, error_callback=back_func_err)
    print('-----')
    p.close()
    p.join()

if __name__ == '__main__':
    get_pool()
    print('ths process is ended')


"""
this is process 9476____
0
test1:3
this is process 9476------
test2:4
this is process 9476------
test3:5
this is process 9476------
this is process 8828____
1
this is process 8936____
2
this is process 9252____
3
this is process 6868____
4
-----
[None, None, None]
[0, 1, 2, 3, 4]
ths process is ended
"""