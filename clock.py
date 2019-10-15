import time
import threading


def clock():
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_min = current_time.tm_min
    current_sec = current_time.tm_sec

    threading.Timer(1, clock).start()


clock()
