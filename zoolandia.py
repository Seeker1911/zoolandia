class Animal(object):

  def __init__(self, name, species):
      self.name = name
      self.species = species

  def get_name(self):
      return self.name

class Species:

  def __init__(self):
    self.common_name = ''
    self.geo_region = ''

class BettaTrifasciata(Species):

  def __init__(self, color):
    self.color = color
    self.common_name = 'Betta'
    self.geo_region = 'Asia'

class Betta(Animal):
  def __init__(self, color, name):
    Animal.__init__(self, name, BettaTrifasciata(color))


class Habitat:

  def __init__(self):
    self.name = ''
    self.members = set ()

  def add_member(self, member):
    self.members.add(member)

  def remove_member(self, member):
    self.members.remove(member)

class Aquarium(Habitat):

  def __init__(self, water_type):
    Habitat.__init__(self)
    self.water_type = water_type

class Walking:

  def __init__(self):
    self.walk_speed = 0
    self.legs = 0

class Flying:

  def __init__(self):
    self.wings = 0

class Swimming:

  def __init__(self):
    self.swim_speed = 0
    self.fins = False
    self.flippers = False
    self.web_feet = False


# The species for a Red Panda
class RedPanda(Animal):

  def __init__(self, name):
    Animal.__init__(self, name, '24 in', '12 lbs')

Fuzzy = RedPanda("fuzzy")

print(Fuzzy.weight)
print(Fuzzy.height)
print(Fuzzy.name)

class Tiger(Animal):

  def __init__(self, name):
    Animal.__init__(self, name, '48 in', '220 lbs')

Cutesy = Tiger("Cutesy")

print(Cutesy.weight)
print(Cutesy.height)
print(Cutesy.name)

class Grizzly(Animal):

  def __init__(self, name):
    Animal.__init__(self, name, '80 in', '300 lbs')

Mike = Grizzly("Mike")

print(Mike.weight)
print(Mike.height)
print(Mike.name)

class Lion(Animal):

  def __init__(self, name, height, weight):
    Animal.__init__(self, name, height, weight)

Simba = Lion('Simba', '60 in', '240 lbs')
print(Simba.name)
print(Simba.height)
print(Simba.weight)
