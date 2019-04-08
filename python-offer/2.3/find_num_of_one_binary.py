
"""
寻找二进制中1个个数
n&n-1的意义
It's figuring out if n is either 0 or an exact power of two.
"""

def num_of_one(n):
    ret = 0
    while n:
        ret += 1
        n = n&n-1
    return ret

print(num_of_one(5))
