# arg **args的用法


def test(l,*arg,**kwarg):
    print('l:',l)
    print(arg)
    print(kwarg)

test (1,2,a =3,b=4)


li =(1,2)
dic = {'a':3,'b':4}
test(*li,**dic)

"""
l: 1
(2,)
{'a': 3, 'b': 4}
l: 1
(2,)
{'a': 3, 'b': 4}
"""