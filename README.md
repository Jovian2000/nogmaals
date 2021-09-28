# nogmaals
## F1.4.02.L1
### Eerste opdracht
```python
aftel = 30
while aftel != 0:
    print("Launching in: "+ str(aftel))
    aftel = aftel - 1 
print("")
print("Ready for takeoff")
```
![test](readme/opdracht1nogmaals.png)
Dit is de aftel opdracht
### Tweede opdracht
```python
time = 1
while time < 13:
    print(str(time) + ":00 am")
    time = time + 1
time2 = 1
while time2 < 13:    
    print(str(time2) + ":00 pm")
    time2 = time2 + 1
```
Dit is de uren opdracht
### Derde opdracht
```python
som = 20
while som < 51:
    print(som)
    som = som + 2
```
dit is de 20 tot 50 opdracht met even getallen
### Vierde opdracht
```python
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
```
Dit is de dagen opdracht
### Vijfde opdracht
```python
number = 1
name = ""
while name != "quit":
    name = input(str(number) + ": ")
    number = number + 1 
```
Dit is de opdracht met als je quit intypt dat de loop eindigt
### Zesde opdracht
```python
number = 50
number2 = number
while number < 1000:
    print(number)
    number2 = number2 + 1
    number = number + number2
```
Dit is de laatste opdracht
