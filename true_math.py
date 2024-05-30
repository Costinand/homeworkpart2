import math


def divide(first, second):

    if second == 0:
        print('(', first, '/',  second, ') = ', math.inf)
    else:
        result = first / second
        print('(', first, '/',  second, ') = ', result),

#import random
#for i in range (5):
    #first = random.randint(1, 10)

    #second = random.randint(0, 5)

    #divide(first, second)
