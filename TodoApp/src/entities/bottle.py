"""Bottle type entity"""
class Bottle:
    """Class that saves all values related to bottle entity"""
    def __init__(self,bottle_type):
        self.bottle_type = bottle_type
        self.deposit = round(self._update_deposit(),2)

    def _update_deposit(self):
        """Updates deposit money to a correct value"""
        if self.bottle_type == "aluminium":
            return 0.15
        if self.bottle_type == "large":
            return 0.40
        if self.bottle_type == "small":
            return 0.20
        if self.bottle_type == "glass":
            return 0.10
        return 0

    def return_deposit(self):
        """Returns the deposit money"""
        return self.deposit

    def return_bottle_type(self):
        """Returns a string that tells what kind of bottle is in question"""
        return self.bottle_type
