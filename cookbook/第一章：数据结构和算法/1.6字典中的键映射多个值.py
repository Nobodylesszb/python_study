"""
一个字典就是一个键对应一个单值的映射。
如果你想要一个键映射多个值，
那么你就需要将这多个值放到另外的容器中， 
比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：

"""
from collections import defaultdict
d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

a = defaultdict(set)
a['a'].add(1)
a['a'].add(2)
a['b'].add(4)