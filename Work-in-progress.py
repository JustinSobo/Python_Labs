# 1. Collect day of week from user.
# 2. Identify charged rate from day of week.
# 3. Collect time of day call started from user.
# 4. Identify charged rate from time of day call started.
# 5. Collect duration of call from user.
# 6. Identify charged rate from duration of call.
# 7. Output total call cost.

call_Day = input("Enter the day the call started at: ")
call_Start = float(input("Enter the time the call started at (hhmm): "))

# Call is between 800-1800
if (call_Start >= 800 and call_Start <= 1800):
    if (call_Day == "Mon" or call_Day == "Tue" or call_Day == "Wed" or call_Day == "Thr" or call_Day == "Fri"):
        call_Rate = float(0.40)
    elif (call_Day == "Sat" or call_Day == "Sun"):
        call_Rate = float(0.15)

# Call is between 0000-759
elif (call_Start >= 0000 and call_Start <= 759):
    if (call_Day == "Mon" or call_Day == "Tue" or call_Day == "Wed" or call_Day == "Thr" or call_Day == "Fri"):
        call_Rate = float(0.25)
    elif (call_Day == "Sat" or call_Day == "Sun"):
        call_Rate = float(0.15)

# Call is between 1801-2359
elif (call_Start >= 1801 and call_Start <= 2359):
    if (call_Day == "Mon" or call_Day == "Tue" or call_Day == "Wed" or call_Day == "Thr" or call_Day == "Fri"):
        call_Rate = float(0.25)
    elif (call_Day == "Sat" or call_Day == "Sun"):
        call_Rate = float(0.15)

call_Duration = float(input("Enter the duration of the call (in minutes): "))
total_Cost = float(call_Duration*call_Rate)

print("This call will cost $%.2f" % total_Cost)
