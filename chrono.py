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


    def tick(self):
        self.current_time = time.localtime()
        self.current_hour = self.current_time.tm_hour
        self.current_min = self.current_time.tm_min
        self.current_sec = self.current_time.tm_sec
        
        if 18 < self.current_hour < 7:
            moon()
        else:
            sun()

        threading.Timer(1, self.tick).start()
