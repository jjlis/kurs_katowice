#Tupla, krotka definiuje się :
krotka = (1, 2.0, 'ala', (4, 5))
print(dir(krotka))
# 'count' _ zlicza wystapienia
#  'index' - zwraca informację o p. czwarte elemencie w krotce
# tuple -> jest to pusta krotka
print(krotka.count('ala'))
print(krotka.count(1))
print(krotka.index(1))
print(krotka.index(1))