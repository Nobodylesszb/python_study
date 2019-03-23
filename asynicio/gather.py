import os
import asyncio

async def target_func3(name):
    """
    :return:
    """
    await asyncio.sleep(1)
    print(name)
    return 0

def run1():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    x = loop.run_until_complete(asyncio.gather(target_func3('A'),target_func3('B'),target_func3('C'),))
    print(x) # 等待返回结果，一个列表，按照事件添加的顺序，但是计算的顺序是不定的
    loop.close()

if __name__ == '__main__':
    run1()


"""
output:
A
B
C
[0, 0, 0]
"""