#pylint: skip-file

"""File not yet in use"""
class Burgers:
    def __init__(self):
        self.type = None

    def buy_meal(self,money):
        if money > 15:
            self.type = "large_meal"
            return money - 15
        if money > 12:
            self.type = "meal"
            return money -12
        if money > 10:
            self.type = "small_meal"
            return money -10
        if money > 8:
            self.type = "large_burger"
            return money -8
        if money > 6:
            self.type = "burger"
            return money -6
        if money > 4:
            self.type = "small_burger"
            return money -4
        if money > 2:
            self.type = "soda"
            return money -2
        return money
