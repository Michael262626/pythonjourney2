import unittest
from gun import Gun

class TestGun(unittest.TestCase):
	def setUp(self):
		self.gun = Gun("Test Gun", 10)

	def test_shoot(self):
		self.assertEqual(self.gun.ammo, 10)
		self.gun.shoot()
		self.assertEqual(self.gun.ammo, 9)
		
		self.assertEqual(self.gun.ammo, 0)
		self.gun.shoot()
		self.assertEqual(self.gun.ammo, 0)

	def test_reload(self):
		self.gun.ammo = 5
		self.gun.reload()
		self.assertEqual(self.gun.ammo, 10)

	def test_gun_is_empty(self):
		self.assertFalse(self.gun.is_empty())
		self.ammo = 0
		self.assertTrue(self.gun.is_empty())

	def test_gun_is_loaded(self):
		self.assertFalse(self.gun.is_empty())
		self.ammo = 10
		self.asserFalse(self.gun.is_empty())