x = 'hello'

y = ''.join(format(ord(i), '08b') for i in x)

print(y)
