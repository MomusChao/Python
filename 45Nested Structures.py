#45 Nested Structures

#print prime number from 2 to 100

i=j=1

#number from 2 to 100
for i in range(2,100,1):
    
    # number can't less than 2
    
    for j in range(2,int(i/j)+1):
        #divisible: break
        if(not i%j):
            break
    if j>i**0.5:
        print('%d is a prime number'%(i))

