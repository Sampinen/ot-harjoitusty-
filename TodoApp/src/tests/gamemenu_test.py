"""Unittests for gamemenu.py"""

import unittest
from gamemenu import GameMenu


class TestGameMenu(unittest.TestCase):
    """Tests for class GameMenu"""

    def setUp(self):
        """Set ups to avoid duplicate code"""
        self.gamemenu = GameMenu()