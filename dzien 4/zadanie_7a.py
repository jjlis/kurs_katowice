lista = [1, 3, 9, 12, 8, 4, 16]

"Napisz uniwersalna funkcje o nazwie select ktora przyjmuje 2 arg " \
"liste oraz funkcje ktora bedzie odpowiadac za to co wybieramy." \
"Funkcja zwraca wybrane wartosci."

def select(lista, func):
    result = []
    for el in lista:
        if func(el):
            result.append(el)
    return result



def test_select():
    assert select(lista, lambda x: x % 2 == 0) == [12, 8, 4, 16]
    assert select(lista, lambda x: x > 10) == [12, 16]