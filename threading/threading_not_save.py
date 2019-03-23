import threading
import time
from threading import Thread

'''
如果是同步运算的话，最终number的结果应该为5000100，
但显然不是。原因是如果线程1取得number=100时，线程切换到线程2，又取得number=100，加1赋值给number=101；如果,又切换回线程1，number加1也是101；
相当于执行了两次加1的操作，然而number=101.这就是多线程的线程非安全！
'''
number = 100
class MyThread(Thread):

    def run(self):
        for i in range(1000000):
            global number
            number += 1
        print(number)

def get_thread1(number=5):
    l_thread = (MyThread() for i in range(number))
    for t in l_thread:
        t.start()

if __name__ == '__main__':
    get_thread1(5)