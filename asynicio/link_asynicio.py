import asyncio
import time
# async 关键字定义一个协程
async def target_func1():
    print('the func start')
    x = await target_func2() # 等待协程完成，控制执行顺序
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

def run():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    x = loop.run_until_complete(target_func1())
    print(x)
    loop.close()
if __name__ == '__main__':
    run()

"""
output:
the func start
the func end2
0
the func end
1

"""