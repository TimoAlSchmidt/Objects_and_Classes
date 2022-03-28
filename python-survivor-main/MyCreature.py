import core
import random

class MyCreature(core.Creature):

  location: list

  def __init__(self, type: str = 'Creature', name: str = 'unknown', color: str = 'white', character: str = 'x'):
      core.Creature.__init__(self, type, name, color, character)
      self.location = [-1,-1]

  def act(self, nearCreatures, nearItems):
    if len(nearCreatures) > 0 and self.attack > 0 and \
      nearCreatures[0].x == self.x and nearCreatures[0].y == self.y:
      self.hit(nearCreatures[0])
    else:
      if not self.grabItemIfNeeded(nearItems):
        self.patrol(9)
        

  def storeCurrentLocation(self):
    self.location[0] = self.x
    self.location[1] = self.y


  def grabItemIfNeeded(self, nearItems):
    for item in nearItems:
      if item.type is core.ItemType.WEAPON:
        if self.attack != 3:
          self.moveTo(item)
          self.storeCurrentLocation()
          return True
        else:
          return False
      if item.type is core.ItemType.HEALTHPACK:
        if self.health < self.MAX_HEALTH:
          self.moveTo(item)
          self.storeCurrentLocation()
          return True
        else:
          return False
      if item.type is core.ItemType.ARMOR:
        if self.defense != 1:
          self.moveTo(item)
          self.storeCurrentLocation()
          return True
        else:
          return False


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


  def moveToLocation(self, place: list):
    x0 = self._x
    y0 = self._y

    x1 = place[0]
    y1 = place[1]

    ans = True

    if x0 < x1:
      self.moveRight()
      ans = False
    elif x0 != x1:
      self.moveLeft()
      ans = False

    if y0 < y1:
      self.moveDown()
      ans = False
    elif y0 != y1:
      self.moveUp()
      ans = False

    return ans


  def patrol(self, distance=0):
    #patrouilleert strak langs de randen van de arena. (zie Wiki: arena.height etc.)
    width = arena.width-1 - distance
    height = arena.height-1 - distance
    x = self._x
    y = self._y
    location = self.location

    #if we have a valid location
    if location[0] != -1:
      if self.moveToLocation(location):
        self.location = [-1, -1]
      else:
        return
    
    if y != distance and y != height:
      if x != distance and x != width:
        if x > distance:
          self.moveLeft()
          return
        elif x < width+1:
          self.moveRight()
          return

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
    

hero = MyCreature(name=":O")

arena = core.Arena(30, 30)
arena.registerCreature(hero)
arena.registerSource(core.Weapon, 0.0001)
arena.registerSource(core.Weapon, 0.0001)
arena.registerSource(core.Weapon, 0.0001)

arena.registerSource(core.Armor, 0.0001)
arena.registerSource(core.Armor, 0.0001)
arena.registerSource(core.Armor, 0.0001)

arena.registerSource(core.HealthPack, 0.0001)
arena.registerSource(core.HealthPack, 0.0001)
arena.registerSource(core.HealthPack, 0.0001)
arena.pause = False
arena.start()