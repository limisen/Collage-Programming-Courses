eng_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
swe_days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

x = input("What day would u like to translate?: ")

z = eng_days.index(x)

if x in eng_days:
    print(swe_days[z])
else:
    print("Please don't forget to capitalise and spell it correctly")