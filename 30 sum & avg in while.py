#30 sum & avg in while

total=0
n=0
ct=-1

while n!=-1:
    ct+=1
    total +=n
    n=eval(input())

print(total)
print(total/ct)

#Shell input some numbers, and use '-1' to break out
