# Zadanie 11
# przykładowy komunikat programu :
# podaj pozycję gracza x: 95
# podaj pozycję gracza y: 95
# gracz znajduje się w prawym górnym rogu


x = 95
y = 95

if x < 0 or y < 0 or x > 100 or y > 100:
    print("poza planszą")
elif x > 90 and y > 90:
    print("PG")
elif x > 90 and y < 10:
    print("DP")
elif x < 10 and y < 10:
    print("DL")
elif x < 10 and y > 90:
    print("PK")
elif x > 90:
    print("Pk")
elif x < 10:
    print("LK")
elif y > 90:
    print("GK")
elif y < 10:
    print("DK")
else:
    print("centrum")