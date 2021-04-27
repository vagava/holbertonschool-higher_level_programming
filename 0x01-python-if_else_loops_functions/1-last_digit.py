#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n_number = number * -1  # convert to positive
    last_digit = (n_number % 10) * -1   # find the last number
else:
    last_digit = number % 10

if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,
                                                                last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif last_digit is not 0 and last_digit < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
                                                                number,
                                                                last_digit))
