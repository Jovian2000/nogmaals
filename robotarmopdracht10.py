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
