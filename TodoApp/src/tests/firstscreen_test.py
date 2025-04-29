"""Unittests for firstscreen.py"""

import unittest
from screens.firstscreen import Screen1
import pygame


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
    
    def test_draw_text_returns_correct_information(self):
        """Checks that """

        self.assertEqual(self.game.draw_text("Moi",100,100),self.game.screen.blit(self.game.font.render("Moi", True, 'black'), (100, 100)))
    
    def test_input_rec_returns_correct_information(self):
        """Checks that input_rect function returns correct information when not active"""
        self.assertEqual(self.game.input_rect(100),pygame.draw.rect(pygame.display.set_mode((1280, 720)), 'dark gray', pygame.Rect(50, 50, max(100, 110), 32), 2))
    
    def test_input_rec_returns_correct_information_when_active(self):
        """Checks that input_rect function returns correct information when active"""
        self.game.active = True
        self.assertEqual(self.game.input_rect(100),pygame.draw.rect(pygame.display.set_mode((1280, 720)), 'red', pygame.Rect(50, 50, max(100, 110), 32), 2))