"""Unittests for gamemenu.py"""

import unittest
from gamemenu import GameMenu


class TestGameMenu(unittest.TestCase):
    """Tests for class GameMenu"""
    def setUp(self):
        """Set ups to avoid duplicate code"""
        self.gamemenu = GameMenu()

    def test_Pygame_is_not_running_in_the_beginning(self):
        """Checks if running variable is set correctly"""
        self.assertEqual(self.gamemenu.IsGameRunning(), False)
