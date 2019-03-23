import time
from multiprocessing import Queue, Process
import os
"""
第一种创建子进程
"""
# def test():
#     time.sleep(2)
#     print('this is process {}'.format(os.getpid()))

# if __name__ == '__main__':
#     p = Process(target=test)
#     p.start() # 子进程 开始执行
#     p.join() # 等待子进程结束
#     print('ths peocess is ended')

"""
output:
this is process 5196
ths peocess is ended

"""

"""
第二种
"""

class MyProcess(Process):

    def run(self):
        time.sleep(2)
        print('this is process {}'.format(os.getpid()))

    def __del__(self):
        print('del the process {}'.format(os.getpid()))

if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('ths process is ended')

"""
output:
ths process is ended
this is process 3464
del the process 3464
del the process 928
"""

"""
总结：
Process对象可以创建进程，但Process对象不是进程，其删除与否与系统资源是否被回收没有直接的关系。

上例看到del方法被调用了两次，Process进程创建时，子进程会将主进程的Process对象完全复制一份，这样在主进程和子进程各有一个Process对象，但是p1.start()启动的是子进程，主进程中的Process对象作为一个静态对象存在。

主进程执行完毕后会默认等待子进程结束后回收资源，不需要手动回收资源；

join()函数用来控制子进程结束的顺序,主进程会阻塞等待子进程结束，其内部也有一个清除僵尸进程的函数，可以回收资源；

当子进程执行完毕后，会产生一个僵尸进程，其会被join函数回收，或者再有一条进程开启，start函数也会回收僵尸进程，所以不一定需要写join函数。

windows系统在子进程结束后会立即自动清除子进程的Process对象，而linux系统子进程的Process对象如果没有join函数和start函数的话会在主进程结束后统一清除。
"""