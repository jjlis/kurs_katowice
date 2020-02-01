import random

#random.seed(10)

#

#Napisz funkcje random_number ktora nie przyjmuje argumentow a zwraca losowa liczbe z przedzialu 1-10.

def random_number():
    return random.randint(1, 101)


print(random_number())

def test_random_number():
    random.seed(0)
    assert random_number() == 50
    random.seed(10)
    assert random_number() == 74