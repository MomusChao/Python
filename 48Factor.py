#48 Factor

Number = input("Enter a number: ")
print("The Factor about %s are:"%Number, end="")

for i in range(1,int(Number)+1):
    if(int(Number)%i!=0):
        continue
    print(i, end=".")
