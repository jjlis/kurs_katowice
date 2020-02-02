# Napisz funkcje largest_difference, ktora przyjmie liste elementow i zwroci najwieksza roznice miedzy nimi
#
# largest_difference([1,2,3, 10]) == 9
# napisz funkcje largest_difference2, ktora zadziala podobnie ale argumenty podajemy osobno a nie w liscie
# largest_difference2(1,2,3, 10) == 9


def largest_difference(elements):
    if elements:
        return max(elements) - min(elements)


def largest_difference2(*elements):
    if elements:
        return max(elements) - min(elements)


def test_largest_difference():
    assert largest_difference([1, 2, 3, 10]) == 9
    assert largest_difference([]) is None
    assert largest_difference([1]) == 0


def test_largest_difference2():
    assert test_largest_difference2(1, 2, 3, 10) == 9
    assert test_largest_difference2() is None
    assert test_largest_difference2(1) == 0
