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
        if position < self.position:
            self.moveLeftTimes(self.position - position)
        elif position > self.position:
            self.moveRightTimes(position - self.position)

    
    def getStackSize(self, position: int = 1):
        position -= 1
        stacks = self._yard
        return len(stacks[position])


    def moveStackTo(self, position: int):
        orig = self.position
        if ((self.getStackSize(position) + self.getStackSize(orig)) < self._maxLayers):
            for i in range(self.getStackSize(orig)):
                self.grab()
                self.moveTo(position)
                self.drop()
                self.moveTo(orig)
            return True
        else:
            return False
        




robotArm = SmartRobotArm()
robotArm.loadMyLevel([["red"],[],[],["yellow", "yellow", "blue", "red"],[]],'moveRightTimes')

# Jouw python instructies zet je vanaf hier:

robotArm.moveTo(4)
robotArm.moveStackTo(1)
robotArm.moveTo(1)
robotArm.moveStackTo(2)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()