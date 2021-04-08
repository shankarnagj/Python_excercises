from datetime import datetime
from datetime import date
from datetime import time
datetime_obj = datetime.now()
print(datetime_obj)
print(f"Current Time : {datetime_obj.time()}")
print("\n")
today = date.today()
print(today)
print(f"Today date : {today.year}")
print(f"Today Month : {today.month}")
print(f"Date Today : {today.day}")

print(dir(datetime))

d = date(2020,8,12)
print(d)

time_stamp = date.fromtimestamp(1262626262)
print(f"Time Stamp is : {time_stamp}")


t = time()
print(t)
print(f"time = {t}")
t1 = time(11,22,59)
print(f"Hour : {t1.hour}")



# current date and time
now = datetime.now()

t2 = now.strftime("%H:%M:%S")
print("time:", t2)

f1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", f1)

f2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", f2)