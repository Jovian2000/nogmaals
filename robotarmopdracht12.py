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
