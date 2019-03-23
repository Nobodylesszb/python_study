import asyncio
import time
from functools import partial

# async 关键字定义一个协程
async def target_func1():
    print('the func end')
    return 1

def get_res(loop):
    print('xxxx')
    loop.stop()

def run1():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    loop.create_task(target_func1())
    # loop.call_soon(partial(get_res, loop)) # 设置回调函数，不能接受返回的参数，需要用到future对象
    # loop.call_soon_threadsafe() # 线程安全的对象
    loop.call_later(delay=5, callback=partial(get_res, loop)) # 异步返回后开始算起，延迟5秒回调
    # loop.call_at(when=8000,callback=partial(get_res, loop)) # 循环开始第8秒回调
    # loop.call_exception_handler() # 错误处理
    loop.run_forever()
    loop.close()

if __name__ == '__main__':
    run1()