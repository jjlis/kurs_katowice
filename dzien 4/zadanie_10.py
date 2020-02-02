# Napisz funckje ktora jako argument przyjmie liste list i zwroci liste bedaca ich polaczeniem.
#
# flatten([[1, 2], [3,4]] -> [1,2,3,4]
# dodatkowo- sprobuj napisac funckcje ktora moze przyjac wiele argumentow, ktore sa listami i zwroci ich polaczenie.


def flatten(*elements):  # Przyklad
    if len(elements) == 1:
        elements = elements[0]
    result = []
    for el in elements:
        result.extend(el)
    return result


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([1, 2], [3, 4]) == [1, 2, 3, 4]
