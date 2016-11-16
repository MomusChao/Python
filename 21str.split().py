#21 str.split()

#str.split([sep=None,maxsplit=-1])
string = 'I have an apple'

print(string.split(sep=' '))
print(string.split())
print(string.split(sep=None))

#return three parts
print(string.split(maxsplit=2))

print(string.split(sep=None,maxsplit=3))
