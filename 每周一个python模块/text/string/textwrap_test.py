import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
print(textwrap.fill(sample_text,width = 50)) # 宽度
"""
output:
     The textwrap module can be used to format
text for output in     situations where pretty-
printing is desired.  It offers     programmatic
functionality similar to the paragraph wrapping
or filling features found in many text editors.

"""

# Removing Existing Indentation

dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
"""
output：
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()

"""
output:
45 Columns:

The textwrap module can be used to format
text for output in situations where pretty-
printing is desired.  It offers programmatic
functionality similar to the paragraph
wrapping or filling features found in many
text editors.

60 Columns:

The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text,width=50)
wrapped += '\n\nSecond paragraph after a blank line'
final = textwrap.indent(wrapped, '> ')
print('Quoted block:\n')
print(final)

"""
output:
Quoted block:

>  The textwrap module can be used to format text
> for output in situations where pretty-printing is
> desired.  It offers programmatic functionality
> similar to the paragraph wrapping or filling
> features found in many text editors.

> Second paragraph after a blank line
"""

## hanging indents

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 10,
                    width=50,
                    ))
"""
The textwrap module can be used to format text for
          output in situations where pretty-
          printing is desired.  It offers
          programmatic functionality similar to
          the paragraph wrapping or filling
          features found in many text editors.
"""

## truncating long text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Original:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShortened:\n')
print(shortened_wrapped)

"""
output:
Original:

 The textwrap module can be used to format text
for output in situations where pretty-printing is
desired.  It offers programmatic functionality
similar to the paragraph wrapping or filling
features found in many text editors.

Shortened:

The textwrap module can be used to format text for
output in situations where pretty-printing [...]
"""