def gen():
    print('start')
    yield 'a'
    print('continue')
    yield 'b'
    print ('end')


for c in gen():
    print('--->',c)

"""
output :

start
---> a
continue
---> b
end

"""