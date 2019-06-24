"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day08_tuples.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn the basics of tuples in python.
"""

# theme = "East", "Bound", "Down"
# type(theme)
# print(theme)
# good = ("Bandit", "Frog", "Snowman")
# type(good)
# print(good)

# theme[0] = "West"

# return_trip = "West", theme[1], theme [2]
# print(return_trip)

movie = ("Smokey and the Bandit", 1977, "Hal Needham",
("Burt Reynolds", "Sally Field", "Jerry Reed"))
title, year, director, stars = movie
bandit, frog, snowman = stars
print("Title: {}\nYear: {}\nDirector: {}".format(title, year, director))
type(stars)
print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))

** i dont understand how stars was generated