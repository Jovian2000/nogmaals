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
