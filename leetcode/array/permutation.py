from itertools import permutations

def permutations_test(str):
    l = list(str)
    res = permutations(l)
    return res

s = 'abc'
print(list(permutations(s)))

