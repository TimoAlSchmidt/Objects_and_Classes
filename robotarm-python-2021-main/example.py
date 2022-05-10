from RobotArm import RobotArm

class SmartRobotArm(RobotArm):

    @property
    def position(self):
        return self._stack + 1

    @property
    def stacks(self):
        return self._yard

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
        return len(self.stacks[position])


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
        

    def getNextColorRight(self, color : str):
        orig = self.position
        while self.position < self._maxStacks:
            try:
                if self.stacks[self.position-1][-1:][0] == color:
                    self.grab()
                    return True
            except:
                pass
            self.moveRight()
        return False


    def getNextColorLeft(self, color : str):
        orig = self.position
        while self.position > 1:
            try:
                if self.stacks[self.position-1][-1:][0] == color:
                    self.grab()
                    return True
            except:
                pass
            self.moveLeft()
        return False





robotArm = SmartRobotArm()
robotArm.randomLevel(10, 1)

# Jouw python instructies zet je vanaf hier:

robotArm.moveTo(10)
robotArm.getNextColorLeft("blue")

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()