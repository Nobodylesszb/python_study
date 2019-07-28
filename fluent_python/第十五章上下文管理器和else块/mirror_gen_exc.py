import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    msg  = ''
    try:
        yield 'JABBERWOR'
    except ZeroDivisionError:
        msg = 'please DO NET DIVER BY ZEAO'

    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

