from RobotArm import RobotArm

class SmartRobotArm(RobotArm):

    @property
    def position(self):
        return self._stack + 1


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

    
    def getStackSize(self, position: int = 1):
        position -= 1
        stacks = self._yard
        return len(stacks[position])




robotArm = SmartRobotArm()
robotArm.loadMyLevel([["red"],[],[],["yellow", "yellow", "blue", "red"],[]],'moveRightTimes')

# Jouw python instructies zet je vanaf hier:

print(robotArm.getStackSize(robotArm.position))
print(robotArm.getStackSize(4))


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()