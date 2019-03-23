import threading
import time
from threading import Thread
number = 100
mutex = threading.Lock() # 创建锁对象

"""
述代码中number += 1是核心代码，这个地方随意切换线程就会造成数据破坏，
因此只要我们能够设置代码每次执行到这里的时候不允许切换线程就行了。这就是锁的由来。
"""

class MyThread(Thread):

    def run(self):
        global number
        for i in range(1000000):
            y = mutex.acquire() # 获取锁
            if y: # 拿到锁就执行下面
                number += 1
                mutex.release() # 释放锁
        print(number)

def get_thread1(number=5):
    l_thread = (MyThread() for i in range(number))
    for t in l_thread:
        t.start()

if __name__ == '__main__':
    get_thread1(5)