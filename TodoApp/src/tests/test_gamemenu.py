import unittest
from gamemenu import GameMenu


class TestGameMenu(unittest.TestCase):
    def setUp(self):
        self.gamemenu = GameMenu()

    def test_Pygame_is_not_running_in_the_beginning(self):
        self.assertEqual(self.gamemenu.IsGameRunning(), False)

    def test_button_changes_color_when_pressed(self):
        return
