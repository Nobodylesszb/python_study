import asyncio
import os

# async 关键字定义一个协程
async def target_func1():
    print('the func start')
    print(os.getpid())
    print('the func end')

def run():
    # 创建一个协程对象
    coroutine = target_func1()
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine) # 将协程对象添加到事件循环，运行直到结束
    print(os.getpid())
    loop.close() # 关闭事件循环


if __name__ == '__main__':
    run()

"""
output:
the func start
7580
the func end
7580

"""