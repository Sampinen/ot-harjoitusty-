import unittest
from entities.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user =User()

    def test_name_is_empty_in_the_beginning(self):
        self.assertEqual(self.user.name,"")

    def test_user_has_no_money_when_initialized(self):
        self.assertEqual(self.user.money,0)

    def test_name_changes_when_a_letter_is_added(self):
        self.user.add_letter("a")
        self.assertEqual(self.user.name,"a")
        self.user.add_letter("b")
        self.assertEqual(self.user.name,"ab")

    def test_changes_correctly_when_remove_letter_is_called(self):
        self.user.add_letter("a")
        self.user.add_letter("b")
        self.user.remove_letter()
        self.assertEqual(self.user.name,"a")

    def test_money_changes_correctly_when_more_is_added(self):
        self.user.update_money(30)
        self.assertEqual(self.user.money,30)
        self.user.update_money(0.37)
        self.assertEqual(self.user.money,30.37)
