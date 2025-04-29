"""Tests for first_screen_button.py"""

import unittest
from buttons import first_screen_buttons as buttons
import pygame

screen = pygame.display.set_mode((1280, 720))
class TestMyButton(unittest.TestCase):
    """Tests for class MyButton"""
    def setUp(self):
        self.button = buttons.MyButton(screen,"Test",100,100)
        pygame.init()
    def test_draw_function_returns_current_phase_when_button_is_not_clicked(self):
        """Draw function should return the first variable given when not clicked"""
        self.assertEqual(self.button.draw(0,1),0)

    def test_draw_function_returns_next_phase_when_button_is_clicked(self):
        """Draw function should return the second variable given when clicked"""
        self.assertEqual(self.button.draw(0,1,debug=True),1)

    def test_check_click_returns_false_when_button_is_not_clicked(self):
        """Check click function should return False when not clicked"""
        self.assertEqual(self.button.check_click(),False)

    def test_check_click_returns_true_when_button_is_clicked(self):
        """Check click function should return True when clicked"""
        self.assertEqual(self.button.check_click(debug=True),True)


class TestOther(unittest.TestCase):
    """Tests for functions not inside any class"""
    def test_collect_bottles_returns_correct_output_when_button_is_not_clicked(self):
        """Collect bottles should return the second value given when not clicked"""
        self.assertEqual(buttons.collect_bottles(screen,0),0)

    def test_collect_bottles_returns_correct_output_when_button_is_clicked(self):
        """Collect bottles should return 2 when not clicked"""
        self.assertEqual(buttons.collect_bottles(screen,0,debug=True),2)

    def test_talk_to_friend_returns_correct_output_when_button_is_not_clicked(self):
        """Talk to a friend should return the second value given when not clicked"""
        self.assertEqual(buttons.talk_to_friend(screen,0),0)

    def test_talk_to_friend_returns_correct_output_when_button_is_clicked(self):
        """Collect bottles should return 3 when not clicked"""
        self.assertEqual(buttons.talk_to_friend(screen,0,debug=True),3)
