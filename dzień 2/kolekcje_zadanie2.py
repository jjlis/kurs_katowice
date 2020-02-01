lista = [1, 2, 3]

print(sum(lista))
print(len(lista))


lista = []

while len(lista) < 10:
    liczba = int(input("podaj liczbę do listy"))
    lista.append(liczba)
    print(lista)
    print(sum(lista))

