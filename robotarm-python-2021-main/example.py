from RobotArm import RobotArm

class SmartRobotArm(RobotArm):
    def moveRightTimes(self, times : int):
        for i in range(times):
            super().moveRight()

robotArm = SmartRobotArm()
robotArm.loadMyLevel([["yellow", "yellow", "blue", "red"],[],[],[],["red"]],'moveRightTimes')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRightTimes(4)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()