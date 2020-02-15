class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))
    def count_total_price(self):
        total_price = 0
        for be in self.products:
            total_price += be.product.price()
        return total_price
    def generate_report(self):
        raport = "Produkty w koszyku"\n
        for be in self.products:
            report +=-{be.product.name} ({be.product.id}), cena:{be.product.price:.2f} x 2
        report += f"W sumie: {self.count_total_price()}"

class BasketEntry:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
    def count_price(self):
        return self.product.price * self.amount

class Product:
    def __init__(self, id, name, price):
        self.name = name
        self.price = price
        self.id = id
        self._add_product = add_product


class TestBasket:

    def test_initialization(self):
        basket = Basket()
        assert basket

    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        product2 = Product(2, "Chleb", 3)
        assert len(basket.products) == 0
        basket._add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].amount == 5
        assert basket.products[0].product == product
        basket._add_product2(product2, 5)
        assert len(basket.products) == 2
        assert basket.products[1].amount == 5
        assert basket.products[1].product == product2

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        product2 = Product(1, "Chleb", 3)
        basket.add_product(product, 10)
        basket.add_product(product2, 3)

    def test_generate_report(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        basket._add_product(product, 2)
        expected = """"Produkty w koszyku:
-Woda (1), cena:10.00 x 2
W sumie: 20.00
""""
        assert basket.generate_report() == expected

class TestProduct:

    def test_initialization(self):
        product = Product(1, "Woda", 10)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10.00


