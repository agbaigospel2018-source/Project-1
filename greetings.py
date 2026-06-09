"""
    to enable the computer greet us with the time of the day, with my name and a hello.
"""

import datetime

date = datetime.datetime.now()
hour = int(date.strftime("%H"))

message = "Good"
name = input("What is your name? ").strip().capitalize()

if hour < 12:
    message += "\tMorning"
elif hour < 16:
    message += "\tAfternoon"
elif hour < 20:
    message += "\tEvening"
else:
    message += "\tNight"
    
print(f"Hello {name}, {message}")