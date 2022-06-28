#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
fizzbuzz()
print("")


def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 and number % 5):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (number % 3):
            print("%s" % (FIZZ), end=' ')
        elif (number % 5):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (number), end=' ')
