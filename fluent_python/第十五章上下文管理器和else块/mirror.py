class LookingGlass:
    def __enter__(self):
        import sys
        self.oringin_write = sys.stdout.write
        sys.stdout.write = self.reaver_write
        return 'jaaverwo'

    def reaver_write(self,text):
        self.oringin_write(text[::-1])

    def __exit__(self,exc_type,exc_value,traceback):
        import sys

        sys.stdout.write = self.oringin_write
        if exc_type is ZeroDivisionError:
            print('DO NOT DIVIDE BY ZEAO')
            return True    