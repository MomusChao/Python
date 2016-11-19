#31 sum & avg in while II

total = 0
n = 0
ct = -1
MaxVal = 0 
MaxPos = 0 

while n!=-1:
    ct += 1
    total += n
    if n>MaxVal:
       Maxval = n
       MaxPos = ct
    n = eval(input())

print(total)
print(total/ct)
print(Maxval)
print(MaxPos)
