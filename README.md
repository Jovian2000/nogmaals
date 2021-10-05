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
``` python
import random
print("Raad het getal tussen 1 en 1000") 
guess = -1 
ronde = 1 
point = 0 
while ronde <= 20: 
    print("Ronde " + str(ronde))
    number = random.randint(1,1000)
    kans = 1  
    while number != guess:
        guess = int(input(str(kans) + ": "))
        if guess < number:
            print("Hoger")
            if (number - guess) <= 20:
                print("Je bent heel warm")
            elif (number - guess) <= 50:
                print("Je bent warm")
        elif guess > number:
            print("Lager")
            if (guess - number) <= 20: 
                print("Je bent heel warm")
            elif (guess - number) <= 50:
                print("Je bent warm")
        else: 
            print("Correct")
            point = point + 1
        kans = kans + 1
        if kans > 10:
            break
    print("Het getal was " + str(number))
    if ronde >= 20:
        break  
    print("Points: " + str(point))
    print("Nog een getal raden? Ja/Nee")
    antwoord = input("")
    if not (antwoord == "Ja" or antwoord == "ja"):
        break
    ronde = ronde + 1
print("Einde!")
print("Uw eindscore is " + str(point))
```
## F1.4.02.O3
### Oefening 7
``` python
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
for movements in range(5):        
    for move in range(6):
        robotArm.moveRight();
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight();
    robotArm.moveRight();

    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```
### Oefening 8
``` python 
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 5


# Jouw python instructies zet je vanaf hier:
robotArm.moveRight();
for move in range(7):
    robotArm.grab()
    for right in range(8):
        robotArm.moveRight();
    robotArm.drop()
    for left in range(8):
        robotArm.moveLeft()
    
    





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```
### Oefening 9 
``` python 
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
for column in range(1,5):
    for count in range(column):
        robotArm.grab()
        for blok in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for blok in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```
### Oefening 10
``` python
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 3


# Jouw python instructies zet je vanaf hier:
for countdown in range(9,0,-2):
    robotArm.grab()
    for move in range(countdown):
        robotArm.moveRight()
    robotArm.drop()
    for move in range(countdown-1):
        robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```
### Oefening 11
``` python 
from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
for move in range(8):
    robotArm.moveRight()    
for colorscan in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()

    
        
    
    


    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```
### Oefening 12
``` python
from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
for movement in range(9,0,-1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for rights in range(movement):        
            robotArm.moveRight()
        robotArm.drop()
        for lefts in range(movement):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
        
                
        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```
### Oefening 13
``` python
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
a = 1
while robotArm.scan() != "":
    for i in range(a):
        robotArm.moveRight()
    robotArm.drop()    
    for i in range(a):
        robotArm.moveLeft()
    robotArm.grab()
    a = a + 1


            


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
```