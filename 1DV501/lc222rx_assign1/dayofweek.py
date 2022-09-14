eng_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
swe_days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

x = input("What day would u like to translate?: ")


if x in eng_days:
    z = eng_days.index(x)
    print(swe_days[z])
elif x not in eng_days:
    print("Please don't forget to capitalise and spell it correctly. Translator only works from english to swedish \n")
else:
    print("Please don't forget to capitalise and spell it correctly. Translator only works from english to swedish \n")
