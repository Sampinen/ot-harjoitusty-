import unittest
from gamemenu import GameMenu


class TestGameMenu(unittest.TestCase):
    def __init__(self):
        self.gamemenu = GameMenu()
    def test_Pygame_is_not_running_in_the_beginning(self):
        self.assertEqual(self.gamemenu.IsGameRunning(),False)
    
    def test_Pygame_is_running_when_menu_is_opened(self):
        self.gamemenu.start_menu()
        self.assertEqual(self.gamemenu.IsGameRunning(),True)

    def test_pygame_window_closes(self):
        return

    def test_button_changes_color_when_pressed(self):
        return
