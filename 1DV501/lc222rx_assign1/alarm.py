#Aquiring the current time
import datetime

timeRN = 0
timeRN = datetime.datetime.now()
timeRN = timeRN.strftime("%H")
print("Current time is: " + timeRN + ":00\n")
timeRN = int(timeRN)

#Aquiring the time the alarm is supposed to be set from now
tillAlarm = int(round(float(input("How long till alarm? (in whole hours): "))))
#Checking so the provided value isnt negative and asks for a new input if that's the case
if tillAlarm <= 0:
    tillAlarm = int(round(float(input("\nCan't set a alarm for a time already passed. \nPlease provide a positive number untill alarm, in whole hours,\nex. 12 or 8, not 16:00, 5h: "))))
    print("\n")
if tillAlarm > 24:
    days = tillAlarm / 24
    roundedDays = int(days // 1)
    hours = days - roundedDays
    hours = round(hours) 

    alarm = (timeRN + hours)
    if alarm >= 25:
        alarm = alarm - 24
        alarm = str(alarm) + ":00"
    if alarm == 24:
        alarm = str(alarm) + ":00" + " or 00:00" 
    else:
        alarm = str(alarm) +  ":00 and " + str(roundedDays) + " days from now"

else: 
    alarm = (timeRN + tillAlarm)
    if alarm >= 25:
        alarm = alarm - 24
        alarm = str(alarm) + ":00"
    if alarm == 24:
        alarm = str(alarm) + ":00" + " or 00:00" 
    else:
        alarm = str(alarm)

#Tells the user when the alarm activates
print("The alarm will go off at: " + alarm)