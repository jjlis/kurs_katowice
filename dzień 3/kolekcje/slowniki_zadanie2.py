# znak = dict()
# litera = 0
# napis = input(f"Podaj napis: ")
# for litera in napis:
#     znak["litera"] = "1"
#     print()

DEVELOPMENT = True
zliczenia = {}

if DEVELOPMENT:
    text = "Ala ma kota"

else:
    text = input(("wpisz tekst"))

# 1
for znak in text:
    if znak in zliczenia:
        zliczenia[znak] += 1
    else:
        zliczenia[znak] = 1
# 2
for znak in text:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

# 3
from collections import defaultdict

zliczenia = defaultdict(int)
for znak in text:
    zliczenia[znak] += 1
print(zliczenia)

#lugosc slownika
print(len(pol_ang))

#sortowanie
print(sorted(pol_ang))

