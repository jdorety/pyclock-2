import time
import threading


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
        print(self.current_sec)
        
        threading.Timer(1, self.tick).start()
