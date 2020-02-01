# ctr alt l

Dni_tygodnia = 7
x = 0
suma_temp = 0
while x < Dni_tygodnia:
    temperatura = int(input("podaj temperaturę"))
    suma_temp += temperatura
    x += 1

print(f"średnia temperatur wynosi: {suma_temp / Dni_tygodnia: .2f}")
