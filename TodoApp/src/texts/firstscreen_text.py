"""Text for firstscreen"""

def say_hi(name):
    """Says nice to meet you and the players name based on text input"""
    return "Hauska tavata "+ name +"!"

def welcome():
    """The text that is printed when the screen is first opened"""
    first = "Tervetuloa peliin! "
    second = "Tässä pelissä tavoitteenasi on kerätä rahaa parta-agamaan. "
    third = "Mikä on sinun nimesi?"
    return first + second + third
def backstory1():
    """First line of text that is printed when you have written your name"""
    first = "Siitä asti kun näit viisivuotiaana lemmikkikaupassa parta-agaman"
    second = ", olet tahtonut sellaisen lemmikiksi."
    return first + second

def backstory2():
    """Second line of text that is printed when you have written your name"""
    first = "Vanhempasi eivät kuitenkaan olleet ideasta tohkeissaan "
    second = "ja et koskaan saanut sellaista lapsena."
    return first + second

def backstory3():
    """Third line of text that is printed when you have written your name"""
    first = "Nyt 20-vuoden jälkeen "
    second = "olet vihdoin päättänyt kerätä rahaa ostaa sellaisen syntymäpäivälahjaksesi."
    return first + second

def your_goal():
    """Fourth line of text that is printed when you have written your name"""
    return "Tavoitteenasi on kerätä 200 euroa. Onnea peliin!"
