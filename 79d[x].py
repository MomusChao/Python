#79 d[x]

dict01 = {1:'a',2:'b'}
print(dict01)

#add 
dict01[3] = 'c'
print(dict01)

#delete
del dict01[3]
print(dict01)

#check key: x in dic
Ans01 = 1 in dict01
print(Ans01)

#check key: x not in dic
Ans02 = 1 not in dict01
print(Ans02)

#iterator: iter(d)
for i in iter(dict01):
    print(i)

#data number: len(d)
print(len(dict01))
