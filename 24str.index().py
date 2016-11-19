#24 str.index()

#str.index(sub[,start[,end]])
string = 'I have an apple, I have a pen.'

#find 'have' index
print(string.index('have'))

#find 'have' index,
print(string.index('have',3))

#find 'have' index. End:index=22(exclude)
#if it couldn't find substring, then return ValueError
print(string.index('have',3,22))
