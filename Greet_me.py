# Printing Good Morning, afternoon and night w.r.t time
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp) 
hour = int(time.strftime('%H'))  # changing the hour from string(default) to integer
print(hour)
minute = time.strftime('%M')
print(minute)
second = time.strftime('%S')
print(second)

if(hour<=12):
    print("Good Morning Ratinder")
elif(hour>12):
    if(hour<=18):
        print("Good Afternoon Ratinder")
    else:
        print("Good Night Ratinder")
