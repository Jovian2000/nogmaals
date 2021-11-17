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
