"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day09_slicing.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn the basics of slicing in python.
"""

quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.", "Is that what you appreciates about me?"]
quotes [0]
print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")
print(f"{quotes[2:5]}")
print(f"{quotes[::2]}")
print(f"{quotes[::-1]}")
quotes [0][::2]
quotes [0][::-1]
print(quotes)
wayne = "Toughest Guy in Letterkenny"
print(wayne [::-1])
print("That's a Texas sized 10-4."[0:9:2])
print(quotes[:])
print(quotes[3:])
print(quotes[:3])
print(quotes[::3])
print(quotes[1] [::-1])
exchange = quotes [2:5]
print(exchange)