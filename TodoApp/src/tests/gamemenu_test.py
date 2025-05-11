#pylint: skip-file
"""Unittests for gamemenu.py"""

import unittest
from screens.gamemenu import GameMenu


class TestGameMenu(unittest.TestCase):
    """Tests for class GameMenu"""

    def setUp(self):
        """Set ups to avoid duplicate code"""
        self.gamemenu = GameMenu()