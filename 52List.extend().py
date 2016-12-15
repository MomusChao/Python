#52 list.extend()

#add ordered object to the last

a = [1,2,3,4]
print(a)

b = ['a','b','c']
a.extend(list(b))
print(a)

a.extend('Hello')
print(a)

