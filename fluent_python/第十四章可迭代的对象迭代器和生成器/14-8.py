def gen_AB():
    print('START')
    yield 'A'
    print('continue')
    yield 'b'
    print('end')


res = [x*3 for x in gen_AB()]

print(res)

for i in res:
    print('--->',i)

"""
output:
START
continue
end
['AAA', 'bbb']

"""

"""
---> AAA
---> bbb
"""

res2 = (x*3 for x in gen_AB())


for i in res2:
    print('---->',i)

"""
START
----> AAA
continue
----> bbb
end
"""
