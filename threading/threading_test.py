import threading
import time
from threading import Thread


"""
我们只需要创建一个Thread对象，并运行start方法，
解释器就会创建一个子进程执行我们的target，我们创建了5个线程，但是使用threading.enumerate查看线程的数量发现有6个线程，
因为当前在执行的还有一个主线程。主线程会默认等待所有的子线程结束后再结束
"""

# def test(x):
#     print('this is {}'.format(x))
#     time.sleep(2)

# def get_thread(number=5):
#     l_thread = (Thread(target=test, args=(i,)) for i in range(number))
#     for t in l_thread:
#         print(t)
#         t.start() # 启动线程开始执行
#     print(len(threading.enumerate()))
# if __name__ == '__main__':
#     get_thread(5)



"""
第二次创建线程
"""
class MyThread(Thread):

    def __init__(self, x):
        super().__init__()
        self.x = x

    def run(self):
        print('this is {}'.format(self.x))
        time.sleep(2)

def get_thread1(number=5):
    l_thread = (MyThread(i) for i in range(number))
    for t in l_thread:
        print(t.name)
        t.start()
    print(len(threading.enumerate()))

if __name__ == '__main__':
    get_thread1(5)