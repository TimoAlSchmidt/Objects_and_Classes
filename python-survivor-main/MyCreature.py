import core
import random

class MyCreature(core.Creature):


  def act(self, nearCreatures, nearItems):
    if len(nearCreatures) > 0 and self.attack > 0 and \
      nearCreatures[0].x == self.x and nearCreatures[0].y == self.y:
      self.hit(nearCreatures[0])
    else:
      self.patrol(9)

  def moveAmountInDirection(self, amount, direction):
    if direction == 0:
      for i in range(amount):
        self.moveUp()
    elif direction == 1:
      for i in range(amount):
        self.moveRight()
    elif direction == 2:
      for i in range(amount):
        self.moveDown()
    elif direction == 3:
      for i in range(amount):
        self.moveLeft()


  def zigzag(self, amount):
    for i in range(amount):
      self.moveLeft()
    for i in range(amount):
      self.moveRight()


  def patrol(self, distance):
    #patrouilleert strak langs de randen van de arena. (zie Wiki: arena.height etc.)
    width = arena.width-1 - distance
    height = arena.height-1 - distance
    x = self._x
    y = self._y

    if y != distance and y != height:
      if x != distance and x != width:
        if x > distance:
          self.moveLeft()
          return
        elif x < width+1:
          self.moveRight()
          return

    if y != distance and y != height:
      if y < distance:
        self.moveDown()
        return
      elif y > height:
        self.moveUp()
        return
    
    if y > distance and x == distance:
      self.moveUp()
      return
    if x < width and y == distance: 
      self.moveRight()
      return
    if y < height and x == width:
      self.moveDown()
      return
    if x > distance and y == height:
      self.moveLeft()
      return


  def __str__(self):
    return f'{self._name} {self._x, self._y}'

  @property
  def _patrolState(self):
    return self._patrolState

hero = MyCreature(name=":O")

arena = core.Arena(30, 30)
arena.registerCreature(hero)
arena.start()