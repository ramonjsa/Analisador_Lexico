def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


for c in char_range(str(chr(0)),str(chr(255))):
    print('(4, \'{}\', 4),'.format(c), end = "")
print('\n')

