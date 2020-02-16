"""
Stworz klase Postac,ktora ma atrybuty: zycie, sila, zwinnosc, obrona, imie.
Przy uzyciu biblioteki Faker stworz mechanizm tworzenia losowych postaci.
pip install faker
Postac w czasie tworzenia jest gdzies umiejscowiona na planszy
Klasa przedmiot- nazwa,bonusy: do_sily, do_obrony
"""
from faker import Faker

fake = Faker("pl_PL")
DEBUG = True

class Postac:
    def atrybuty(self):
        self.name = name
        self.zycie = fake.random.randit(1, 101)
        self.sila = fake.random.randit(1, 101)
        self.zwinnosc = fake.random.randit(1, 101)
        self.obrona = fake.random.randit(1, 101)

    @classmethod
    def with_fake_name(cls):
        return cls(fake.name())

    def __str__(self):
        return f"<{self.name}| e: {self.zycie}, s: {self.sila}, a: {self.zwinnosc}, d:{self.obrona}>"

    @property
    def zyje(self):
        if self.zycie > 0:
            return True
        return False

    def otrzymaj_obrazenia(self, moc_ciosu):
        print("Otrzymuje obazenia:", moc_ciosu)
        self.zycie -= moc_ciosu

    def zadaj_obrazenia(self):
        return fake.random.randit(1, self.sila)

    @staticmethod
    def walka(postac, postac2):


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    @classmethod
    def random(cls):
        return cls(fake.random.randit(1,10))
class Polozenie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Przedmiot:
    def __init__(self, name, bonus):
        self.name = name
        self.do_sily = fake.random.randint(1, 20)
        self.do_obrony = fake.random.randint(1, 20)


postac = Postac("Zenek")
postac2 = Postac.with_fake_name()
siekiera = Przedmiot("Krwawa siekiera")
while postac.zyje and postac2.zyje:
    print(f"Uderza:{postac2.name}")
    postac.otrzymaj_obrazenia(postac2.zadaj_obrazenia())
    print(f"Uderza:{postac.name}")
    postac2.otrzymaj_obrazenia(postac.zadaj_obrazenia())
print(f"{postac.imie} {postac.zyje}")
print(f"{postac2.imie} {postac2.zyje}")

    if postac.polozenie == postac2.polozenie:
        print("Konfrontacja!!!")
        wynik = Postac.walka(postac, postac2)
        if wynik is False:
            beak
    if postac.polozenie == siekiera.polozenie:
        print(f"Znalazlem :{siekiera}")
        wynik =