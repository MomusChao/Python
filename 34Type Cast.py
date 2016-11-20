#34 Type Cast

str1 = '72'
#decomal
print(int(str1))
#Octal
print(int(str1, 8))
#hexadecimal
print(int(str1,16))

print(type(str1))

str2 = int(str1)
print(type(str2))

str3 = float(str2)
print(type(str3))
