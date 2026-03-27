# Customized Greeting Based on Real Time of Day
from datetime import datetime

def get_daytime(t):
    if 5 <= t <= 11:
        return "Good Morning"
    elif 12 <= t <= 17:
        return "Good Afternoon"
    elif 18 <= t <= 21:
        return "Good Evening"
    else:
        return "Good Night"

current_hour = datetime.now().hour
greeting = get_daytime(current_hour)
print(greeting)

print("Greeting code has completed.")

