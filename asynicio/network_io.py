# 使用asyncio+aiohttp,如果想异步化，网络请求需要抛弃requests包
import asyncio
import time
from aiohttp import ClientSession

async def target2():
    print('start2')
    async with ClientSession() as session:
        async with session.get(url='http://www.baidu.com') as rsp:
            data = await rsp.read()
    print('end2')
    return data

def run1():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    tasks = [target2() for i in range(100)]
    ts = asyncio.gather(*tasks)
    t = time.time()
    loop.run_until_complete(ts)
    print(time.time()-t)
    loop.close()

if __name__ == '__main__':
    run1()