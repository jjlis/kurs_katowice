n = 10
warunek = n % 2 == 0
if warunek :  # True albo False - do tego się sprowadza warunek
    print("podzielne")
else:
    print("nieparzyste")
if n % 2 == 0:
    print("podzielne")
else:
    print("nieparzyste")
print("po ifie")

if n % 3 == 0:
    print("podziele przez 3")
else:
    print("pozostałe przypadki")


import datetime

datetime.datetime.now()
x = 2020
rok = int(input("podaj rok urodzenia"))
wynik = x - rok
if wynik > 18:
    print("pełnoletni")
else:
    print("niepełnoletni")
