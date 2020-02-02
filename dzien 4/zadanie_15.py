# Napisz funkcje ktora dla zadanej liczby zwroci pare liczb- o jeden mniejsza i wieksza nazwij funkcje up_down
# up_down(5)->(4,6)

def up_down(liczba):
    return (liczba - 1), (liczba + 1)


def test_up_down():
    assert up_down(5) == (4, 6)
