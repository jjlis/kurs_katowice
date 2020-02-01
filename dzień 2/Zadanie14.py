# liczba_min = 0  -> 0 nie może byc min.
# None określa nieznane dane
liczba_min = None
if liczba_min is None:
    print("Tak")

# is True is False is None

x = "Napis 1"
y = "Napis 1"

# id -> jest to identyfikator obiektu w pamięci
print(id(x), id(y))
# is jest głębszym porównaniem bierze równiez pod uwagę identyfikator pamięci. Stosoway w szczegolności w : None, True, False
x == y
x is y

#zadanie 14
#liczba_min = None
#liczba = int(input("podaj liczbe"))
#while liczba <=

while True:
    polecenie = input("Podaj liczbę lub wpisz k by zakończyć")
    if polecenie == 'k':
        break
    liczba = int(polecenie)
    if liczba_min is None or liczba < liczba_min:
        liczba_min = liczba
    if liczba_max is None or liczba > liczba_max:
        liczba_max = liczba_max
if liczba_max is None:
            print("nie podano liczby")
else:
            print("Maximum: ", liczba_max)
            print("Minimum: ", liczba_min)