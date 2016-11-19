#28 n! II
n=eval(input())
sum=0

for i in range(1,n+1):
    sum+=i
    print(i, end="")
    if(i<n):
       print("+", end="")
print(' =',sum)
