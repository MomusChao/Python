#33 str.format()

#str.format(*args,**kwargs)
#formatting calculation

a = '{}+{}={}'
print(a)
print(a.format(10,5,10+5))

b = '{ID},{Name}'
print(b)
print(b.format(ID=531125, Name='Momus'))

c = '{1}+{2}={0}'
print(c)
print(c.format(4+5,4,5))
