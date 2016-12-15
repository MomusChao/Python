#77 Frozenset()

a = frozenset({1,2,3,4})
print(a,type(a))
b = {1,2}
c = a-b
print(c,type(c))

#You can't change the set
#a.add(2)

