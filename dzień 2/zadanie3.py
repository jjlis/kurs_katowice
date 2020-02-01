# Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej liście liczb całkowitych

lista = [12, 35, 65, 78, -54, -23, -34, -90,]
ld = 0
lu = 0

for el in lista:
    if el < 0:
        lu +=1
    else:
        ld +=1

print(f"licz dodatnich{ld}, licz ujemnych{lu}")

