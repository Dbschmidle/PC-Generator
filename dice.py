from random import randint

def rollxdy(y, x=1):
    value = 0
    for i in range(x):
        value += randint(1, y)

    return value