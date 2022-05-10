from RobotArm import RobotArm

class SmartRobotArm(RobotArm):

    @property
    def position(self):
        return self._stack

    def moveRightTimes(self, times : int):
        for i in range(times):
            super().moveRight()

    def moveLeftTimes(self, times : int):
        for i in range(times):
            super().moveLeft()

    def moveTo(self, position : int):
        if position < self.position:
            self.moveLeftTimes(self.position - position)
        elif position > self.position:
            self.moveRightTimes(position - self.position)

robotArm = SmartRobotArm()
robotArm.loadMyLevel([["yellow", "yellow", "blue", "red"],[],[],[],["red"]],'moveRightTimes')

# Jouw python instructies zet je vanaf hier:

robotArm.moveTo(6)
robotArm.moveTo(0)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()