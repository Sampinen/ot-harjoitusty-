"""Unittests for bottle_generator.py"""
import unittest
import pygame
from bottle_generator import BottleGenerator, Bottle

screen = pygame.display.set_mode((1280, 720))
class BottleTest(unittest.TestCase):
    """Tests for class Bottle"""
    def setUp(self):
        self.aluminium_can = Bottle(screen,"aluminium")
        self.large_plastic_bottle = Bottle(screen,"large")
        self.small_plastic_bottle = Bottle(screen,"small")
        self.glass_bottle = Bottle(screen,"glass")

    def test_aluminium_can_has_correct_deposit(self):
        self.aluminium_can.draw()
        self.assertEqual(self.aluminium_can.check_deposit(), 0.15)

    def test_large_plastic_bottle_can_has_correct_deposit(self):
        self.large_plastic_bottle.draw()
        self.assertEqual(self.large_plastic_bottle.check_deposit(), 0.40)

    def test_small_plastic_bottle_can_has_correct_deposit(self):
        self.small_plastic_bottle.draw()
        self.assertEqual(self.small_plastic_bottle.check_deposit(), 0.20)

    def test_glass_bottle_can_has_correct_deposit(self):
        self.glass_bottle.draw()
        self.assertEqual(self.glass_bottle.check_deposit(), 0.10)
    # def test_is_clciked_returns_deposit_money_when_clicked(self):
    #     self.aluminium_can.test_click()
    #     self.assertEqual(self.aluminium_can.is_clicked(),0.15)
class BottleGeneratorTest(unittest.TestCase):
    """ Tests for class BottleGenerator"""
    def setUp(self):
        self.bottle_generator = BottleGenerator()
    def test_generating_bottles_increases_bottle_list_size(self):
        """when generate_bottles function is called, the lenght of bottle_list increases"""
        self.assertEqual(self.bottle_generator.how_many_bottles(),0)
        self.bottle_generator.generate_bottles(screen)
        self.assertGreater(self.bottle_generator.how_many_bottles(),0)