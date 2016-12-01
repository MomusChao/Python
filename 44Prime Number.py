#44 prime number

number = input("Please input a number:")
i = 2
prime = 0

#i<= square root of number
while(i<=int(number)**0.5):
    if(int(number)%i == 0):
        prime = 1
    i+=1

if(prime == 1):
  print("%s is not a prime"%number)
else:
  print("%s is a prime number"%number)
