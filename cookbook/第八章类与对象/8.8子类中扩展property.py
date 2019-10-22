class Person:
    def __init__(self,name):
        print('get name')
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("not a str")
        self._name = value
        
    @name.deleter
    def name(self):
        raise AttributeError("can't delete name")

if __name__ == "__main__":
    p = Person('test')
    print(p.name)