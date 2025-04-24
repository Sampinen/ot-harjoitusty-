import unittest
import pygame
from bottle_generator import BottleGenerator, Bottle

screen = pygame.display.set_mode((1280, 720))
class BottleTest(unittest.TestCase):
    def setUp(self):
        self.aluminium_can = Bottle(screen,"aluminium")
        self.large_plastic_bottle = Bottle(screen,"large")
        self.small_plastic_bottle = Bottle(screen,"small")
        self.glass_bottle = Bottle(screen,"glass")
    
class BottleGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.bottle_generator = BottleGenerator()
    def test_generating_bottles_increases_bottle_list_size(self):
        self.assertEqual(self.bottle_generator.how_many_bottles(),0)
        self.bottle_generator.generate_bottles(screen)
        self.assertGreater(self.bottle_generator.how_many_bottles(),0)
    