#40 List


#40-1
numbers = [0,4,2,3]

#change the content of a list
numbers[3] = 5
print(numbers)

#add "10"
numbers.append(10)
print("append:",numbers)

#insert "7"
numbers.insert(4,15)
print("insert:",numbers)

#remove "15"
numbers.remove(15)
print("remove:",numbers)

#sort
numbers.sort()
print("sort:",numbers)



#40-2
b =["A","B","C",1,"2"]
print(3*b)

for i in b:
    print(i)

for i in b:
    print(i*3)
