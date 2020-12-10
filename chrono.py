import time
import threading
from moon import moon
from sun import sun


def is_it_day(current_min, current_hour, wake_up_time, bed_time):
    if current_hour > wake_up_time['hour'] and current_hour < bed_time['hour']:
        return True
    elif current_hour == wake_up_time['hour'] and current_min >= wake_up_time['minute']:
        return True
    elif current_hour == bed_time['hour'] and current_min < bed_time['minute']:
        return True
    else:
        return False


class Chrono:

    def __init__(self):
        self.current_time = time.localtime()
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        self.bedtime = {'hour': 21, 'minute': 50}
        self.wakeup = {'hour': 6, 'minute': 0}
        self.daytime = is_it_day(
            self.current_min, self.current_hour, self.wakeup, self.bedtime)
        if self.daytime == True:
            sun()
        else:
            moon()

    def tick(self):
        self.current_time = time.localtime()
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        self.check_time()
        print(self.current_hour, self.current_min)
        print(self.daytime)

        threading.Timer(1, self.tick).start()

    def check_time(self):
        bt = self.bedtime
        wu = self.wakeup
        daytime = is_it_day(self.current_min, self.current_hour, wu, bt) # check if daytime
        if daytime == True and self.daytime == False:
            self.daytime = True  # toggle daytime to True
            sun()  # display sun on UnicornHat
        elif daytime == False and self.daytime == True:
            self.daytime = False  # set daytime to False
            moon()  # display moon on UnicornHat
