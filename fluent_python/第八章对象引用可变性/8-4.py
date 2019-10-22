import copy

class  BUS:
    def __init__(self,passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self,name):
        self.passengers.append(name)
    
    def drop(self,name):
        self.passengers.remove(name)


if __name__ == "__main__":
    bus1 = BUS(['ALICE','BILL','DAVID','BOB'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    # 输出 41685680 41685904 41687696
    bus1.drop('BOB')
    print(bus1.passengers, bus2.passengers, bus3.passengers)
    # 输出 ['ALICE', 'BILL', 'DAVID'] ['ALICE', 'BILL', 'DAVID'] ['ALICE', 'BILL', 'DAVID', 'BOB']