inputday = input("Welke dag? ")
day = ""
while inputday != day:    
    if day == "maandag":
        day = "dinsdag"
    elif day == "dinsdag":
        day = "woensdag"
    elif day == "woensdag":
        day = "donderdag"
    elif day == "donderdag":
        day = "vrijdag"
    elif day == "vrijdag":
        day = "zaterdag"
    elif day == "zaterdag":
        day = "zondag"
    else:
        day = "maandag"
    print(day)
