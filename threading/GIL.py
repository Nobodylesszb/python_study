import threading
import time
from threading import Thread

number = 100
number1 = 100
mutex = threading.Lock()

"""
全局锁的存在是为了保护多线程对数据的安全访问；
对于任何Python程序，不管有多少的处理器内核，任何时候都总是只有一个线程在执行；
全局锁的存在使得一般情况下多线程比单线程的执行速度慢；
python程序只有在io密集时多线程代码效率有所提高，所以不推荐使用多线程而是多进程；更好的替代方案为协程
"""
class MyThread(Thread):

    def run(self):
        global number
        t1 = time.time()
        for i in range(1000000):
            y = mutex.acquire() # 获取锁
            if y: # 拿到锁就执行下面
                number += 1
                mutex.release() # 释放锁
        t2 = time.time()
        print(t2-t1)

def get_thread1(number=5):
    l_thread = (MyThread() for i in range(number))
    for t in l_thread:
        t.start()

def get_thread2(n=5):
    global number1
    for i in range(1000000*n):
        number1 += 1
    print(number1)

if __name__ == '__main__':
    get_thread1()
    t2 = time.time()
    get_thread2()
    t3 = time.time()
    print(t3-t2)