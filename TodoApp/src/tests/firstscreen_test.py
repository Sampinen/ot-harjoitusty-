"""Unittests for firstscreen.py"""

import unittest
from screens.firstscreen import Screen1
import pygame


class TestScreen1(unittest.TestCase):
    """Tests for class Screen1"""

    def setUp(self):
        self.game = Screen1()
    
    def test_input_rec_returns_correct_information(self):
        """Checks that input_rect function returns correct information when not active"""
        self.assertEqual(self.game.input_rect(100),pygame.draw.rect(pygame.display.set_mode((1280, 720)), 'dark gray', pygame.Rect(50, 75, max(100, 110), 32), 2))
    
    def test_input_rec_returns_correct_information_when_active(self):
        """Checks that input_rect function returns correct information when active"""
        self.game.active = True
        self.assertEqual(self.game.input_rect(100),pygame.draw.rect(pygame.display.set_mode((1280, 720)), 'red', pygame.Rect(50, 75, max(100, 110), 32), 2))