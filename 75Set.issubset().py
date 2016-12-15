#75 Set.issubset()

# if set is a subset of set2? Return Bool
#set.issubset(set2)

cities01 = {'Taipei', 'Tokyo','New York'}
print(cities01,'\n',sep="")
cities02 = {'Hanoi'}
print(cities02,'\n',sep="")

Ans01 = cities02.issubset(cities01)
print(Ans01,'\n',sep="")


print("====================")
print(cities01,'\n',sep="")
cities03 = {'Taipei'}
print(cities03,'\n',sep="")
Ans02 = cities03.issubset(cities01)
print(Ans02,'\n',sep="")
