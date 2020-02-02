# Napisz funkcje, ktora przyjmie dwa argumenty - dwie liczby i zwroci informacje, czy pierwszy argument jest podzielny przez drugi.
# Pozwol na podanie 1 argumentu - wtedy domyslnie spawdzamy czy dzielnikiem jet 2
# div(10,5) -> True
# div(10,3) -> False
# div(10) -> True

def div(a: int, b: int = 2) -> bool:
    return a % b == 0



def test_div():
    assert div(10, 5) is True
    assert div(10, 3) is False
    assert div(10) is True
