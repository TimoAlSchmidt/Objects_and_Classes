from RobotArm import RobotArm

class SmartRobotArm(RobotArm):
    def moveRightTimes(self, times : int):
        for i in range(times):
            super().moveRight()

    def moveLeftTimes(self, times : int):
        for i in range(times):
            super().moveLeft()

robotArm = SmartRobotArm()
robotArm.loadMyLevel([["yellow", "yellow", "blue", "red"],[],[],[],["red"]],'moveRightTimes')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRightTimes(4)
robotArm.moveLeftTimes(3)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()