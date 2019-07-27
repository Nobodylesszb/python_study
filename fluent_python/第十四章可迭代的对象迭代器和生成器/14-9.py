class ArithmeticProcession:
    def __init__(self,bigin,step,end =None):
        self.bigin = bigin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.bigin + self.step)(self.bigin)
        forever = self.end is None
        index = 0 
        while forever or result < self.end:
            yield result
            index += 1
            result = self.bigin + self.step * index

        