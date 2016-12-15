#81 Get LocalTime
import time;

localtime = time.asctime( time.localtime(time.time()) )
print("Local Time :", localtime)
