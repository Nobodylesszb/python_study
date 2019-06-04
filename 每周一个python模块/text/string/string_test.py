import string
 
# s = 'The quick brown fox jumped over the lazy dog.'
 
# print(s)
# print(string.capwords(s))

"""
The quick brown fox jumped over the lazy dog.
The Quick Brown Fox Jumped Over The Lazy Dog.
"""


# template
values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

"""
output:
TEMPLATE: 
Variable        : foo
Escape          : $
Variable in text: fooiable
"""
