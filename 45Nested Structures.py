#45 Nested Structures

i=j=1
for i in range(2,100,1):
    # number can't less than 2
    #i/j divisor have 2, then break
    for j in range(2,int(i/j)+1):
        if(not i%j):
            break
    if j>i**0.5:
        print('%d is a prime number'%(i))

