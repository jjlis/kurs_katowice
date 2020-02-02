data = [1, 2, 3, 4, 5, 6, 7]


def przytnij(data, start, stop):
    result = []
    dodawaj = False
    for d in data:
        if start(d):
            dodawaj = True
        if dodawaj:
            wynik.append(d)
            if stop(d):
                break


return result


def test_przytnij():
    assert przytnij(data=[1, 2, 3, 4, 5, 6, 7], start=lambda x: x > 3, stop=lambda x: x == 6) == [4, 5, 6]
