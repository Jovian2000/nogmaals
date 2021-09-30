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
## F1.4.02.L2
``` python
# name of student: Jovian
# number of student: 99047257
# purpose of program: bedoeling is dat de programma helpt met terug te geven van de juiste hoeveelheid munten van bepaalde soort
# function of program: Het rekent uit hoeveel wisselgeld je terugkrijgt en laat zien welke munten je terug krijgt
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # Hier vragen ze hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # Hier vragen ze hoeveel je hebt betaalt
change = paid - toPay # Hier doen ze wat je hebt betaald min wat je moet betalen, dat word dan de variabel change

if change > 0: # als de change groter is dan nul dan draait hij het volgende
  coinValue = 500 # hier word bepaald dat de coin value 500 is
  
  while change > 0 and coinValue > 0: # Zolang de change groter is dan 0 EN de coinvalue groter dan 0 dan rolt hij het volgende totdat de het niet meer zo is
    nrCoins = change // coinValue # Deze functie zorgt dat als je 2 getallen deelt en het komt niet precies uit, dat hij de getallen achter de komma wegwerkt en altijd omlaag afrond
    
    if nrCoins > 0: 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: Deze if statement zit in de while lus dus hij rolt eigenlijk deze statement totdat hij op nul springt 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50   
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
```
## F1.4.02.O2
