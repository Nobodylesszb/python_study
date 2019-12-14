# User = type('user',(),{})
# user = User()
# print(type(user))


def say(self, content = 'world'):
    print('hello',content)

User = type('User', (), {'name':'apple', 'say':say})
user = User()
print(user.say()) # Hello world
print(user.__dict__) # {}
print(User.__dict__) # 输出见下图：
"""
hello world
None
{}
{'name': 'apple', 'say': <function say at 0x105b2a1e0>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None}
"""
