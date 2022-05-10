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
        position -= 1
        if position < self.position:
            self.moveLeftTimes(self.position - position)
        elif position > self.position:
            self.moveRightTimes(position - self.position)

    
    def getStackSize(self, position : int = 1):
        position -= 1
        stacks = self._yard
        print(len(stacks[position]))


robotArm = SmartRobotArm()
robotArm.loadMyLevel([[],[],["yellow", "yellow", "blue", "red"],[],["red"]],'moveRightTimes')

# Jouw python instructies zet je vanaf hier:

robotArm.getStackSize(1)
robotArm.getStackSize(3)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()