
class Pojazd:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def poruszaj_sie(self):
        print("Porusza sie")

    def stop(self):
        print("Pojazd zatrzymal sie")

class Statek(Pojazd):
    def plyn(self):
        self.poruszaj_sie()
        print("Plynie")

class Samochod(Pojazd):
    def jedz(self):
        self.poruszaj_sie()
        print("Jedzie...")

class Amfibia(Statek, Samochod):
    pass
prom = Statek("Batory")
prom.plyn()
prom.stop()
samochod = Samochod("Ford")
samochod.jedz()
samochod.stop()

amfibia = Amfibia("Lola")
amfibia.jedz()
amfibia.plyn()
amfibia.stop()

#metody klasowe
import datetime
class Osoba:

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

def osoba_z_rok_ur(imie, rok_ur):
    wiek = datetime.datetime.now().year - rok_ur
    return Osoba(imie, wiek)


os = Osoba("Anna", 25)
os2