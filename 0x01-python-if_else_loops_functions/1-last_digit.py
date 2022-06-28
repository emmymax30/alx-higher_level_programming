#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if x > 6:
    print("{} last digit of " number " is " x "and is greater than 6 and not 0".format(number))
elif x == 0:
    print("{} last digit of " number " is " x " and is 0".format(number))
else:
    print("{} last digit of " number " is " x "and is less than 6 and not 0".format(number))
