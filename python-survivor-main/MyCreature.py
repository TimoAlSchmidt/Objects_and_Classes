import core
import random

class MyCreature(core.Creature):


  def act(self, nearCreatures, nearItems):
    if len(nearCreatures) > 0 and self.attack > 0 and \
      nearCreatures[0].x == self.x and nearCreatures[0].y == self.y:
      self.hit(nearCreatures[0])
    else:
      self.patrol()
      pass

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

  def patrol(self):
    #patrouilleert strak langs de randen van de arena. (zie Wiki: arena.height etc.)
    width = arena.width-1
    height = arena.height-1
    x = self._x
    y = self._y

    if x != 0 and y != 0 and x != width and y != height:
      self.moveLeft()
      print("moveLeft")
    elif x == 0 and y != 0:
      self.moveUp()
      print("moveUp")
    elif x != width and y == 0:
      self.moveRight()
      print("moveRight")
    elif x == width and y != height:
      self.moveDown()
      print("moveDown")
    elif x != 0 and y == height:
      self.moveLeft()
      print("moveLeft")


  def __str__(self):
    return f'{self._name} {self._x, self._y}'

  @property
  def _patrolState(self):
    return self._patrolState

hero = MyCreature(name=":O")

arena = core.Arena(5, 3)
arena.registerCreature(hero)
arena.start()