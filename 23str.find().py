#23 str.find()

#str.find(sub[,start[,end]])
string = 'I have an apple, I have a pen.'

#find 'have' index
print(string.find('have'))

#find 'have' index,
print(string.find('have',3))

#find 'have' index. End:index=22(exclude)
#if it couldn't find substring, then return -1
print(string.find('have',3,22))
