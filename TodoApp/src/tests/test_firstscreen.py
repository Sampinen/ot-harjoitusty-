"""Unitteests for firstscreen.py"""

from firstscreen import Screen1
import unittest


class TestScreen1(unittest.TestCase):
    """Tests for class Screen1"""
    def setUp(self):
        self.game = Screen1()

    def test_money_is_zero_in_the_beginning(self):
        """Checks the amount of money"""
        self.assertEqual(self.game.get_money(), 0)

    def test_name_is_empty_in_the_beginning(self):
        """Checks that the name variable is initialized correctly"""
        self.assertEqual(self.game.get_name(), "")

    def test_say_hi_returns_correct_string(self):
        """Checks that the function returns a correct string"""
        self.game.set_name("Matti")
        self.assertEqual(self.game.say_hi(), "Hauska tavata Matti!")

    def test_backstory1_returns_correct_string(self):
        """Checks that the function returns a correct string"""
        self.assertEqual(self.game.backstory1(
        ), "Siitä asti kun näit viisivuotiaana lemmikkikaupassa parta-agaman, olet tahtonut sellaisen lemmikiksi.")

    def test_backstory2_returns_correct_string(self):
        """Checks that the function returns a correct string"""
        self.assertEqual(self.game.backstory2(
        ), "Vanhempasi eivät kuitenkaan olleet ideasta tohkeissaan ja et koskaan saanut sellaista lapsena.")

    def test_backstory3_returns_correct_string(self):
        """Checks that the function returns a correct string"""
        self.assertEqual(self.game.backstory3(
        ), "Nyt 20-vuoden jälkeen olet vihdoin päättänyt kerätä rahaa ostaa sellaisen syntymäpäivälahjaksesi.")

    def test_your_goal_returns_correct_string(self):
        """Checks that the function returns a correct string"""
        self.assertEqual(self.game.your_goal(), "Tavoitteenasi on kerätä 200 euroa. Onnea peliin!")
