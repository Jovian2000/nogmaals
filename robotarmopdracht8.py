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
