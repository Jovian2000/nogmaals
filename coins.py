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