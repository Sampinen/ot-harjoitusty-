import unittest
from entities.bottle import Bottle
class BottleTest(unittest.TestCase):
    def setUp(self):
        self.aluminium = Bottle("aluminium")
        self.large = Bottle("large")
        self.small = Bottle("small")
        self.glass = Bottle("glass")
        self.wrong = Bottle("Broken_bottle")

    def test_aluminium_can_has_correct_deposit(self):
        self.assertEqual(self.aluminium.return_deposit(),0.15)

    def test_large_bottle_has_correct_deposit(self):
        self.assertEqual(self.large.return_deposit(),0.40)

    def test_small_bottle_has_correct_deposit(self):
        self.assertEqual(self.small.return_deposit(),0.20)

    def test_glass_bottle_has_correct_deposit(self):
        self.assertEqual(self.glass.return_deposit(),0.10)

    def test_bottle_with_incorrect_type_returns_no_deposit(self):
        self.assertEqual(self.wrong.return_deposit(),0)
