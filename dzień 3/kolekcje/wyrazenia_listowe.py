# wynik = []
# for el in range(10):
#     if el % 2 == 0:
#         wynik.append(el ** 3)
#
# print(wynik)
#
# print([(el, el ** 3) for el in range(10)])
#
# print([(el, el ** 3) for el in range(10) if el % 2 == 0])

#Zadanie 13


print([i/10 for i in range(0,11)])

print({(i, i** 2, i**3) for i in range (-10, 10) })

napisy = set(["aa", "aaaaa", "aaaaaaaaa"])
print({napis: len(napis) for napis in napisy})