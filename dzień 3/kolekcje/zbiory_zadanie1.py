liczby = set()

while True:
    polecenie = input ("Wprowadz liczbe lub k aby zakonczyc")
    if polecenie == "k":
        break
    liczby.add(int(polecenie))

parzyste = set(range(0, 101, 2))
print(f"""
Liczby unikalych: {len(liczby)}
W tym parzystych z przedzialu 0-100: {len(liczby & parzyste)}""")





