import asyncio
import sys
from aiohttp import web

@asyncio.coroutine
def init(loop,address,port):
    app = web.Application(loop=loop)
    app.router.add_route('get','/','home')
    handler = app.make_handler()
    server = yield from loop.create_server(handler,address,port)
    return server.sockets[0].getsockname()

def main(address='127.0.0.1',port = 8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop,address,port))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])