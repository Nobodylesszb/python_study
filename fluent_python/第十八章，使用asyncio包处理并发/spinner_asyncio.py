import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    write,flush = sys.stdout.write,sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        status = char + '' +msg
        write(status)
        flush()

        write('\x08'*len(status))
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
        write(' '*len(status) + '\x08' * len(status))