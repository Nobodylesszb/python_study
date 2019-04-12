some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])

# some_tuple[2] = 'change this'
# """
# TypeError: 'tuple' object does not support item assignment
# """
another_tuple[2].append(1000)
print(another_tuple)
# another_tuple[2] += [99,999]
"""
output:
([1, 2], [3, 4], [5, 6, 1000])
TypeError: 'tuple' object does not support item assignment
"""