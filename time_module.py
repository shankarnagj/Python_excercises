import time

current_time = time.localtime()
current_time = time.strftime("%H:%M:%S", current_time)
print(current_time)

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)