import time
import threading
from moon import moon
from sun import sun


class Chrono:

    def __init__(self):
        self.current_time = time.localtime()
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        self.daytime = bool
        self.bedtime = [19, 0]
        self.wakeup = [6, 0]

        # TODO: remember to set checks for minutes later on

    def tick(self):
        self.current_time = time.localtime()
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        self.check_time()

        threading.Timer(1, self.tick).start()

    def check_time(self):
        bt = self.bedtime
        wu = self.wakeup
        if (wu[0] <= self.current_hour < bt[0]) and self.daytime is not True:
            self.daytime = not True  # toggle daytime to True
            sun()  # display sun on UnicornHat
        elif (wu[0] > self.current_hour or self.current_hour >= bt[0]) and self.daytime:
            self.daytime = not False  # set daytime to False
            moon()  # display moon on UnicornHat
