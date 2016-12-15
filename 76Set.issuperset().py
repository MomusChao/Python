#76 Set.issuperset()

# if set2 is a subset of set? Return Bool
#set.issubset(set2)

cities01 = {'Taipei', 'Tokyo','New York'}
print(cities01,'\n',sep="")
cities02 = {'Hanoi'}
print(cities02,'\n',sep="")

Ans01 = cities01.issuperset(cities02)
print(Ans01,'\n',sep="")


print("====================")
print(cities01,'\n',sep="")
cities03 = {'Taipei'}
print(cities03,'\n',sep="")
Ans02 = cities01.issuperset(cities03)
print(Ans02,'\n',sep="")
