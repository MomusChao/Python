#86 Except

#try...except...(else...finally)
i = 100
for j in range(3,-4,-1):
    try:
        print('%d/%d=%0.1f'%(i,j,i/j))
    except ZeroDivisionError:
        print('Divisor is 0, can not use Division!!')
              
