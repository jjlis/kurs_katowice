lista = [3, 4, 2, 6, 1, 8]

for indeks_podstawienia in range(len(lista)):
    indeks_min_wart = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wart]:
            indeks_min_wart = indeks_ogona
    lista[indeks_podstawienia], lista[indeks_min_wart] = lista[indeks_min_wart], lista[indeks_podstawienia]  # a,b= b,a

assert lista == [0, 1, 2, 3, 4, 5]
