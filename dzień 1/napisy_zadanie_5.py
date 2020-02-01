Miasto_A = input("podaj nazwę miasta A")
Miasto_B = input("podaj nazwę miasta B")
Dystans = int(input(f "dystans między {Miasto_A}-{Miasto_B}: "))
Cena = float(input("cena paliwa: "))
Spalanie = float(input("spalanie na 100km: "))

print()
koszt przejazdu = (Dystans * Spalanie * Cena / 100)

print(f"koszt przejazdu {Miasto_A}-{Miasto_B}")
