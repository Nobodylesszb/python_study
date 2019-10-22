class Student:
    def __getattr__(self, item):
        print('call getattr')
        return item + ' is not exits'

    def __setattr__(self, key, value):
        print('call setattr')
        self.__dict__[key] = value

    def __getitem__(self, item):
        print('call getitem')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

if __name__ == "__main__":
    s = Student()
    print(s.name)