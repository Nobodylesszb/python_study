from array import array
import reprlib
import math
import functools
import operator
import itertools
import numbers

class Vector:
    typecode = 'd'
    def __init__(self,components):
        self._components = array(self.typecode,components)

    def __mul__(self,scalar):
        if isinstance(scalar,numbers.Real):
            return Vector(n * scalar for n in self._components)
        else:
            return NotImplemented
    
    def __rmul__(self,scalar):
        return self * scalar

    def __matmul__(self,other):
        """
        实现点积
        """
        try:
            return sum(a*b for a, b in zip(self,other))
        except TypeError:
            return NotImplemented
        
    def __rmatmul__(self,other):
        return self @ other 

    def __eq__(self,other):
        """
        重新实现__eq__的方法
        """
        return (len(self) == len(other)) and all(a ==b for a,b in zip(self,other))

    


        
