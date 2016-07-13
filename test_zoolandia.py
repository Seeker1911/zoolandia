import unittest
import zoolandia

class TestAnimal(unittest.TestCase):
	"""docstring for TestAnimal"""
	@classmethod
	def setUpClass(self):
		pass

	def test_animal_creation(self):
		bob = zoolandia.Betta('orange', 'Bob') 
		self.assertEqual(a_animal.species.color, 'orange')
		self.assertEqual(a_animal.name, 'Bob')
		self.assertIsInstance(bob, zoolandia.Animal)
		self.assertIsInstance(bob.species, zoolandia.Species)
		self.assertIsInstance(bob.species, zoolandia.BettaTrifasciata)

class TestSpecies(unittest.TestCase):
	def test_commonname_empty_string_default(self):
		species = zoolandia.Species()
		self.assertEqual(species.common_name, '')

	def test_georegion_empty_string_default(self):
		species = zoolandia.Species()
		self.assertEqual(species.geo_region, '')

class TestHabitat(unittest.TestCase):
	"""docstring for TestHabitat"""
	def test_habitat_empty_string_default(self):
		habitat = zoolandia.Habitat()
		self.assertEqual(habitat.name, '')

	def test_habitat_empty_string_default(self):
		habitat = zoolandia.Habitat()
		self.assertIsInstance(habitat.members, set)

	def test_add_member(self):
		habitat = zoolandia.Aquarium('freshwater')
		nemo = zoolandia.Betta('orange', 'nemo')
		aquarium.add_member(nemo)
		self.assertNotIn(nemo, aquarium.members)

	def test_remove_member(self):
		aquarium = zoolandia.Aquarium('freshwater')
		bob = zoolandia.Betta('orange', 'Bob')
		aquarium.add_member(nemo)
		aquarium.remove_member(nemo)
		self.assertIn(bob, aquarium.members)



class TestWalking(unittest.TestCase):
	"""docstring for TestHabitat"""
	def test_legs_zero_default(self):
		walking = zoolandia.Walking()
		self.assertEqual(walking.legs, 0)

	def test_walk_speed_zero_default(self):
		walking = zoolandia.Walking()
		self.assertEqual(walking.walk_speed, 0)

class TestSwimming(unittest.TestCase):
	"""docstring for TestHabitat"""
	def test_appendages(self):
		swimming = zoolandia.Swimming()
		self.assertEqual(swimming.swim_speed, 0)
		self.assertFalse(swimming.fins)
		self.assertFalse(swimming.flippers)
		self.assertFalse(swimming.web_feet)

class TestFlying(unittest.TestCase):
	"""docstring for TestHabitat"""
	def test_wings_zero_default(self):
		flying = zoolandia.Flying()
		self.assertEqual(flying.wings, 0)

if __name__ == '__main__':
	unittest.main()
