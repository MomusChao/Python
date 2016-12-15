#78 dict

#key:value
# four ways to create dictionary
dict01 = {1:'a',2:'b'}
dict02 = dict({1:'a',2:'b'})
dict03 = dict(zip((1,2),('a','b')))
dict04 = dict([[2,'b'],[1,'a']])

#is: is the same object?
print(dict01 is dict02)
print(dict01 is dict03)
print(dict01 == dict02)
print(dict01 == dict03)
print(dict01 == dict04)
