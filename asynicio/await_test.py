import os
import asyncio
import time

async def target_func1():
    print('the func start')
    x = await target_func2() # 当前协程挂起
    print(x)
    print('the func end')
    return 1

async def target_func2():
    """
    目标函数2
    :return:
    """
    time.sleep(2)
    print('the func end2')
    return 0

