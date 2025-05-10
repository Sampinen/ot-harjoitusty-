"""Unittests for bottle_generator.py"""
import unittest
import pygame
from event_logic.bottle_generator import BottleGenerator, DrawBottle

screen = pygame.display.set_mode((1280, 720))
class DrawBottleTest(unittest.TestCase):
    """Tests for class Bottle"""
    def setUp(self):
        self.aluminium_can = DrawBottle(screen,"aluminium")
        self.large_plastic_bottle = DrawBottle(screen,"large")
        self.small_plastic_bottle = DrawBottle(screen,"small")
        self.glass_bottle = DrawBottle(screen,"glass")
    def test_is_clicked_returns_deposit_money_when_clicked(self):
        """Checks that is_clicked returns the right amount of money"""
        self.aluminium_can.draw()
        self.assertEqual(self.aluminium_can.is_clicked(debug=True),0.15)
    def test_check_click_returns_true_when_clicked(self):
        """Makes sure that check_click function returns the correct value"""
        self.aluminium_can.draw()
        self.assertEqual(self.aluminium_can.check_click(debug=True),True)
class BottleGeneratorTest(unittest.TestCase):
    """ Tests for class BottleGenerator"""
    def setUp(self):
        self.bottle_generator = BottleGenerator()
    def test_generating_bottles_increases_bottle_list_size(self):
        """when generate_bottles function is called, the lenght of bottle_list increases"""
        self.assertEqual(self.bottle_generator.how_many_bottles(),0)
        self.bottle_generator.generate_bottles(screen)
        self.assertGreater(self.bottle_generator.how_many_bottles(),0)
    def test_is_clicked_removes_one_bottle_from_the_list(self):
        """Makes sure that the bottle is removed from the list after clicked"""
        self.bottle_generator.generate_bottles(screen)
        bottles_in_the_beginning = self.bottle_generator.how_many_bottles()
        self.bottle_generator.is_clicked(self.bottle_generator.bottle_list()[0], debug=True)
        self.assertEqual(self.bottle_generator.how_many_bottles(),bottles_in_the_beginning-1)
    def test_is_clicked_returns_deposit_money_when_clicked(self):
        """Checks that function is clicked returns deposit money with positive value when clicked"""
        self.bottle_generator.generate_bottles(screen)
        self.bottle_generator.bottle_list()[0].draw()
        self.assertGreater(self.bottle_generator.is_clicked(self.bottle_generator.bottle_list()[0], debug=True),0)

    def test_is_clicked_returns_zero_when_not_clicked(self):
        """Checks that is_clicked returns zero when bottle is not clicked"""
        self.bottle_generator.generate_bottles(screen)
        self.bottle_generator.bottle_list()[0].draw()
        self.assertEqual(self.bottle_generator.is_clicked(self.bottle_generator.bottle_list()[0]),0)

    def test_check_bottles_returns_zero_when_bottle_not_clicked(self):
        """Checks that check bottles returns zero when bottle is not clicked"""
        self.bottle_generator.generate_bottles(screen)
        self.assertEqual(self.bottle_generator.check_bottles(),0)

    def test_check_bottles_returns_positive_value_when_bottle_is_clicked(self):
        """Checks that check bottles returns positive value when bottle is clicked"""
        self.bottle_generator.generate_bottles(screen)
        self.assertGreater(self.bottle_generator.check_bottles(debug=True),0)
