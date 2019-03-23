
import os
import asyncio

async def target_func1():
    print('the func start')
    print(os.getpid())
    print('the func end')
coroutine = target_func1()

try:
    coroutine.send(None) # 唤醒协程
except StopIteration:
    print('xx')
    coroutine.close() # 关闭

"""
output:
the func start
9376
the func end
xx
"""