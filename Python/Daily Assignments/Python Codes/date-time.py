# Using date and time functions
from datetime import datetime, timedelta

current_time = datetime.now()
print(current_time)

future_time = current_time + timedelta(days=7)
print(future_time)
