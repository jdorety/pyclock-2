import time
import threading
from moon import moon
from sun import sun
from christmas_tree import christmas_tree


class Chrono:

    def __init__(self, bedtime_hour, bedtime_minute, wakeup_hour, wakeup_minute):
        self.current_time = time.localtime()
        self.display_time = time.strftime("%a, %b %d; %H:%M")
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        self.current_month = self.current_time.tm_mon
        self.current_day = self.current_time.tm_min
        self.daytime = bool
        self.bedtime = self.convert_to_minutes(bedtime_hour, bedtime_minute)
        self.wakeup = self.convert_to_minutes(wakeup_hour, wakeup_minute)

    def tick(self):
        self.current_time = time.localtime()
        self.display_time = time.strftime("%a, %b %d; %H:%M")
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        # self.current_month = self.current_time.tm_mon
        # self.current_day = self.current_time.tm_mday
        self.current_month = 12
        self.current_day = 25

        self.check_time()
        print(self.current_month, self.current_day)

        threading.Timer(1, self.tick).start()

    def convert_to_minutes(self, hour, minutes):
        return (hour * 60) + minutes

    def check_time(self):
        t = self.convert_to_minutes(self.current_hour , self.current_min)
        bt = self.bedtime
        wu = self.wakeup
        # if (wu[0] <= self.current_hour < bt[0]) and (wu[1] <= self.current_min < bt[1]) and self.daytime is not True:
        if (wu <= t < bt) and self.daytime is not True:
            self.daytime = True  # toggle daytime to True
            self.determine_day_pic(self.current_month, self.current_day)  # display sun on UnicornHat
        # elif ((wu[0] > self.current_hour and wu[1] > self.current_min) or (self.current_hour >= bt[0] and self.current_min >= bt[1])) and self.daytime:
        elif (wu > t or t >= bt) and self.daytime:
            self.daytime = False  # set daytime to False
            moon()  # display moon on UnicornHat

    def change_bedtime(self, hour, minute):
        if type(hour) == int and type(minute) == int:
            self.bedtime = self.convert_to_minutes(hour, minute)
            return { "success": True, "message": "Success!"}
        else:
            return { "success": False, "message": "Invalid params"}
    
    def determine_day_pic(self, month, day):
        if (day == 25 and month ==12):
            christmas_tree()
        else:
            sun()