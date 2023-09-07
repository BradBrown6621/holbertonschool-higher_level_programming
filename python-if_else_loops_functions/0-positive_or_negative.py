#!/usr/bin/python3
import random
number = random.randint(-10, 10)
polarity = ""
if (number > 0):
    polarity = "positive"
elif (number < 0):
    polarity = "negative"
else:
    polarity = "zero"
print("{} is {}".format(number, polarity))
