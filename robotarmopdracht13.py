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
