class PacPerson:
    def __init__(self, lives, direction=0, invincible=False, timeInvincibleRemaining=0, ghostsEaten = 0):
        self.lives = lives
        self.direction = direction
        self.invincible = invincible
        self.timeInvincibleRemaining = timeInvincibleRemaining
        self.ghostsEaten = ghostsEaten
    
    def update():
        pass

    def move(direction):
        pass

    def turnInvincible(time):
        pass

    def die():
        pass

    def killGhost(ghost):
        pass

    def playerRespawn():
        pass

    def eatPellet(pellet):
        pass

    def collisionCheck():
        pass



class Ghost:
    def __init__(self, ghostType, color="", speed=0, alive=True, respawnTimer=0, fleeing=False):
        self.ghostType = ghostType
        if color != "":
            self.color = color
        else:
            pass

        if speed != 0:
            self.speed = speed
        else:
            pass

        self.alive = alive
        self.respawnTimer = respawnTimer
        self.fleeing = fleeing

    def update():
        pass

    def move(direction):
        pass

    def die():
        pass

    def playerRespawn():
        pass




pacMan = PacPerson(lives=3)

pinky = Ghost(ghostType="Pinky", color="pink", speed=5)
blinky = Ghost(ghostType="Blinky", color="orange", speed=7)
