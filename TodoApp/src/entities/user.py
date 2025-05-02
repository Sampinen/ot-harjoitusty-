"""Class for saving user information"""
class User:
    """Saves all variables related to user"""
    def __init__(self):
        self.money = 0
        self.name = ""

    def update_money(self,money: float):
        """Adds the given value to the total money"""
        self.money += money
        round(self.money,2)

    def return_money(self):
        """Returns the amount of money the user has"""
        return round(self.money,2)

    def update_name(self,name: str):
        """Updates the name of the user"""
        self.name =name

    def return_name(self):
        """Returns the name of the user"""
        return self.name

    def add_letter(self,letter: str):
        """Adds a single letter to username"""
        self.name +=letter

    def remove_letter(self):
        """Removes a single letter from the username"""
        self.name = self.name[:-1]
