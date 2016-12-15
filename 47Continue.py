#47 continue

#from 1 to 100, and skip "3"

i = 0
while i<100:
    i+=1
    if(i%3 == 0 or (i-30<10 and i-30>0)or((i-3)%10 ==0)):
        continue
    print()
    print(i,end="")
