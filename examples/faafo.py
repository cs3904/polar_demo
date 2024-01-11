import time
import sys
import datetime
import os
import time
import thread
if __name__ == '__main__':
    args = sys.argv[1:]
    hour = int(args[1])
    minute = int(args[2])
    second = int(args[3])
    # print(interval)
    # rn = str(datetime.datetime.now().time())
    # wait(1)
    # sys.exit()
    #start new thread here 
        thread = Thread(target = set_alarm, args = (hour, minute, second))
        thread = Thread(target = [insert name of image function], args = ())
def set_alarm(hour, minute, second):

    now = datetime.datetime.now()
    print(now)    # Choose 6PM today as the time the alarm fires.
    print(time.localtime().tm_hour)
    # This won't work well if it's after 6PM, though.
    alarm_time = datetime.datetime.combine(now.date(), datetime.time(hour, minute, second))
    print(alarm_time)
    # Think of time.sleep() as having the operating system set an alarm for you,
    # and waking you up when the alarm fires.
    time.sleep((alarm_time - now).total_seconds())

    print("still doing stuff")
    os._exit()