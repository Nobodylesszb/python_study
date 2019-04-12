# array = [1, 8, 15]
# g = (x for x in array if array.count(x) > 0)
# array = [2, 8, 22]
# print(list(g))
# """
# output:
# [8]
# """

# array_1 = [1,2,3,4]
# print(id(array_1))
# g1 = (x for x in array_1)
# array_1 = [1,2,3,4,5]
# print(id(array_1))
# print(list(g1))

# """
# 35149064
# 35147912
# [1, 2, 3, 4]
# """

array_2 = [1,2,3,4]
array_3 = array_2[:]
print(id(array_2))
print(id(array_2[:]))
print(id(array_3))
# g2 = (x for x in array_2[:])
array_2[:] = [1,2,3,4,5]
# g2 = (x for x in array_2[:])
g2 = (x for x in array_2)
print(id(array_2[1:3]))
print(id(array_2[:]))
print(list(g2))


"""
39998728
39998920
39997576
39998920
39998920
[1, 2, 3, 4, 5]
"""

