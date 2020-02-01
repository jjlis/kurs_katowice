# + - / *
liczba1 = int(input("podaj liczbe 1:"))
liczba2 = int(input("podaj liczbe 2:"))
operacja = int(input("działanie:"))

if operacja == "+":
    wynik = liczba1 + liczba2
elif operacja == '-':
    wynik = liczba1 - liczba2
elif operacja == '*':
    wynik = liczba1 * liczba2
elif operacja == '/':
    # ask for permission
    if liczba2 == 0:
        wynik = "nie dziel przez zero"
    else:
        wynik = liczba1 / liczba2

        #beg for forgivenes
        #try:
        #     wynik = liczba1 / liczba2
        # except zeroDivisionError:
        #     wynik = "nie dziel przez zero"
else:


