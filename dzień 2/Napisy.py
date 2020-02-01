#napis = "Ala ma kota"

#for litera in napis:
#    print(litera)

#"a" in napis
#napis[1:]

#zadanie 7 Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y,) w podanym przez użytkownika napisie.

napis = "Ala ma kota"

samogłoski = "aeiouy"

licznik = 0

Napis = input("podaj słowo")
for litera in napis.lower():
    if litera in samogłoski:
        licznik += 1
