#80 time

import time;

ticks = time.time()
#show seconds
print("Number of ticks since 12:00am, Jan.1, 197\0:",ticks)


#clock(): return float
clock01 = time.clock()
#sleep(seconds)
time.sleep(1)
clock02 = time.clock()
time.sleep(1)
clock03 = time.clock()
time.sleep(1)
print('clock01 is:', clock01)
print('clock01 is:', clock02)
print('clock01 is:', clock03)



#https://docs.python.org/3/library/time.html
