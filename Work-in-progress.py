# 1. Collect day of week from user.
# 2. Identify charged rate from day of week.
# 3. Collect time of day call started from user.
# 4. Identify charged rate from time of day call started.
# 5. Collect duration of call from user.
# 6. Identify charged rate from duration of call.
# 7. Output total call cost.


call_Day = input("Enter the day the call started at: ")

if (call_Day == "Mon"):
    print("The day is Mon")
elif (call_Day == "Tue"):
    print("The day is Tue")
elif (call_Day == "Wed"):
    print("The day is Wed")
elif (call_Day == "Thr"):
    print("The day is Thr")
elif (call_Day == "Fri"):
    print("The day is Fri")
elif (call_Day == "Sat"):
    print("The day is Sun")
elif (call_Day == "Sun"):
    print("The day is Sun")



call_Start = float(input("Enter the time the call started at (hhmm): "))

if (call_Start >= 800 and call_Start <= 1800):
    print("Call is between 800-1800")
elif (call_Start >= 0000 and call_Start <= 759):
    print("Call is between 0000-759")
elif (call_Start >= 1801 and call_Start <= 2359):
    print("Call is between 1801-2359")



call_Duration = input("Enter the duration of the call (in minutes): ")

