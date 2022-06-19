import datetime
import time

b = datetime.datetime.fromtimestamp(time.time()).strftime('%c')

print(b)