#18 String

a = 'Hello Momus'

print(a)
#print from s[2] to the end
print(a[2:])

#a[0:5}: print from a[0] to a[4] without a[5]
print(a[0:5]+' and Hi '+a[6:11])

#print from s[0] to the end, and the seperation is 2
print(a[::2])

#print conversely
print(a[::-1])

#print from a[-1] to a[1] without a[0], and the seperation is -2
print(a[-1:0:-2])
