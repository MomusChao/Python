#06 input()

a = input('Input your name:')
#confirm this data type is str
print(type(a))

#Division
#input():get str
#eval(): change data type from str to int
print('Now is division test')
b1 = eval(input('Numerator:'))
b2 = eval(input('Denominator:'))
print(type(b1),type(b2))

print('Answer:',end='')
print(b1/b2)
