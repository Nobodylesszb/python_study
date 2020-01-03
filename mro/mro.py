class Base:
    def __init__(self):
        print('This is Base init function')
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('This is init function of A')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('This is init function of B')

class C(A,B):
    def __init__(self):
        #super().__init__(self)
        A.__init__(self)
        B.__init__(self)
        print('This is init function of C')


if __name__ == "__main__":
    c = C()

"""
output:
This is Base init function
This is init function of A
This is Base init function
This is init function of B
This is init function of C
"""

    