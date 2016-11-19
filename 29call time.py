#29 Call time
import time
def GetTime(fm):
    #print(fm)
    return time.strftime(fm)
t = GetTime('%Y-%m-%d %H:%M:%S')

#Shell input:t
