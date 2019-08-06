import threading
import asyncio

#创建任务方式
@asyncio.coroutine
def hello():
    print('Start Hello', threading.currentThread())
    yield from asyncio.sleep(5)
    print('End Hello', threading.currentThread())


@asyncio.coroutine
def world():
    print('Start World', threading.currentThread())
    yield from asyncio.sleep(3)
    print('End World', threading.currentThread())

# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), world()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
Start World <_MainThread(MainThread, started 17276)>
Start Hello <_MainThread(MainThread, started 17276)>
End World <_MainThread(MainThread, started 17276)>
End Hello <_MainThread(MainThread, started 17276)>
"""