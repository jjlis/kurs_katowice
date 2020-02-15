class Product:
    def __init__(self, ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return f"<Product {self.ID}, {self.nazwa}, {self.cena}>"
    def print_info(self):
        print(f"Product \"{self.name} \", id: {self.id}, cena: {self.price}")
Product = Product("1", "Woda", "10.99")

Product.print_info()
