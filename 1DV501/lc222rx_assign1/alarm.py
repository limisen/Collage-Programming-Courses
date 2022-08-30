import datetime

x = datetime.datetime.now()
x = x.strftime("%H")
# print(x)

timeRN = int(input("What time is it? "))

tillAlarm = float(input("How long till alarm? "))

alarm = (timeRN + tillAlarm)

if alarm < 25 and (tillAlarm >= 0):
    alarm = alarm - 24
elif tillAlarm >= 0:
    tillAlarm = float(input("How long till alarm? "))

print("The alarm will go off at: " + str(alarm))