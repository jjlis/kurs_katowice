# Napisz funkcje o nazwie: only_ints ktora przyjmie 2 argumenty a i b i zwroci true jesli oba sa intami w przeciwnym razie zwroci False.


def only_inst(a, b):
    return type(a) == int and type(b) == int



def test_only_inst():
    assert only_inst(1, 2) == True
    assert only_inst("a", 1) == False
    assert only_inst(1, True) == False




