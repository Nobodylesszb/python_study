import collections


class doppelDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    dd = doppelDict(one=1)
    print(dd)
    dd['tow'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
