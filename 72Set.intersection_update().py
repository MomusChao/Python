#72 Set.intersection_update()

#set.intersection_update(set2)
cities01 = {'Taipei', 'Tokyo','New York'}
print(cities01,'\n',sep="")
cities02 = {'Hanoi', 'Tokyo','Berlin'}
print(cities02,'\n',sep="")


cities01.intersection_update(cities02)
print(cities01,'\n',sep="")
