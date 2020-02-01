ceny = dict(ziemniaki="2",  # ????
            chleb="5",
            pomidory="6.5",
            ser="3.2"
            )

w_magazynie = dict(ziemniaki="3",  # ????
                   chleb="5",
                   pomidory="6.5",
                   ser="3.2"
                   )
while True:
    sciezka = input("Zakup [z]?, Magazyn[m]")
    if sciezka == "z":
        print("Witaj, dzis oferujemy:")
        for produkt, cena in ceny.items():
            print(f"- {produkt} - {cena} PLN")

        co = input("Co chcesz kupic?")
        cena = ceny.get(co)
        if not cena:
            print("Takiego produktu nie oferujemy!")

        else:
            ile = int(input(f"Ile chcesz kupic [{co}]"))
        koszt = cena * ile
        print(f"Nalezy sie: {koszt}")
    else:
        # print("W magazynie sa dostepne: ")
        # for produkt, cena in ceny_m.items():
        #     print(f"-{produkt} -{cena} PLN")
        #     co = input
        co = input("Co chcesz dodac?")
        ile = int(input(f"Ile dodajesz [{co}]?"))
        cena = input(f"Jaka cena za [{co}] (enter by pominac)?")
        w_magazynie[co] = w_magazynie.get(co, 0) + ile
        if cena:
            ceny[co] = float(cena)
