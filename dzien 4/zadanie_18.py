def formatuj(*args, **kwargs):
    text = "\n".join(args)
    for alowo, wartosc in kwargs.items():
        klucz = "$" +slowo
        text = text.replace(klucz, wartosc)
        return test

# formatuj(
#     "koszt $cena PLN",
#     "kwota $cena brutto",
#     "podatek: $podatek %",
#     cena=10,
#     podatek=20
# )
# print(formatuj
# print(napis)
#
#
# def test_formatuj():
#     assert formatuj("Koszt 10 PLN") is True
#     assert formatuj("Kwota 10 brutto") is True
#     #assert formatuj("Podatek 20%") is True
