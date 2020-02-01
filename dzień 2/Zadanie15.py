import random
DEBUG = True
Wymiar_planszy = 10

gracz_x = random.randint(1, Wymiar_planszy)
gracz_y = random.randint(1, Wymiar_planszy)

skarb_x = random.randint(1, Wymiar_planszy)
skarb_y = random.randint(1, Wymiar_planszy)

od1_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
while True:

    ruch = input("w którą stronę?(wsad):")
    if ruch == "w":
        gracz_y += 1
    elif ruch == "s":
        gracz_y -= 1
    elif ruch == 'a':
        gracz_x -= 1
    elif ruch == 'd':
        gracz_x += 1
    if gracz_x < 1 or gracz_x > Wymiar_planszy or gracz_y < 1 or gracz_y > Wymiar_planszy:
        print("jesteś po za plansza")
        break
od1_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

if od1_po_wylosowaniu == 0:
        print("wygrana!")
        break

    if od1_przed > od1_po:
        print("ciepło")
    else:
        print("zimno")

print("Koniec!")


