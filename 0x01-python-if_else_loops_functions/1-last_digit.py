#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    positive = number * -1
else:
    positive = number
last = positive % 10
if number < 0 and last != 0:
    print('Last digit of', number, 'is -{:d}'.format(last),
          'and is less than 6 and not 0')
else:
    print('Last digit of', number, 'is', last, end='')
    if last > 5:
        print(' and is greater than 5')
    elif last == 0:
        print(' and is 0')
    else:
        print(' and is less than 6 and not 0')
