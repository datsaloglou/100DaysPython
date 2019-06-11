"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day04_variables.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn about using variables in python.
"""

greeting = "Hello"
_name = "General Kenobi."
Greeting = "There"
_bestLine_ep3_ = "You are a bold one."
print(greeting + " "+ Greeting + "\n\t" + _name + " "+ _bestLine_ep3_)
print("{} {} \n\t {} {}".format(greeting, Greeting, _name, _bestLine_ep3_))
released = 2005
print("Revenge of the Sith was released on May 4, " + str(released) + ".")
print("Revenge of the Sith was release on May 4, {}.".format(released))
a = 3
b = 4
c = a ** 2 + b ** 2
print("Pythagorean theorem: a^2 + b^2 = c^2, so when a = {} and b = {}, then c = {}".format(a, b, c))
film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())
var = "Variables are mutable"
type(var)
var = 3
type(var)
var = 3.5
var = int(var)
type(var)
var = str(var)
var = float(var)
type(var)
var = True
type(var)
