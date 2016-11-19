#27 formatting

#print('text%x'%(tmp))

a = 7134
b = 8635.2235
c = 'Momus'
d = 97

#decimal
print('This is %d'%(a))
#decimal & %in string
print('This is %d%%'%(a))

#float in decimal
print('This is %f'%(b))
#round it to the nearest hundredth
print('This is %4.2f'%(b))

#float & scientific notation in decimal
print('This is %e'%(b))
print('This is %E'%(b))

#Octal
print('This is %o'%(a))

#Hexadecimal
print('This is %x'%(a))
print('This is %X'%(a))

#str
print('This is %s'%(c))

#take the first 3 bytes
print('This is %.3s'%('Momus'))

#chr
print('This is %c'%(d))

#string by repr()
print('This is %r'%(c))
