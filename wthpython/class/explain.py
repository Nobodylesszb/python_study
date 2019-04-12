class Crazy(object):
  def __init__(self): print("I")
  def __del__(self): print("D")

print(Crazy() is Crazy())
"""
output:
I
I
D
D
False
"""

print(id(Crazy()) == id(Crazy()))
"""
output:
I
D
I
D
True
"""