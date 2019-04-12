class Crazy:
  pass

print(Crazy() == Crazy())
print( Crazy() is Crazy())
print(hash(Crazy()) == hash(Crazy()))
print(id(Crazy()) == id(Crazy()))
"""
output:
False
False
True
True
"""
