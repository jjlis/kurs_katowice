def kwadraty(n):# w nawiasie dajemy argumenty
   wynik = [i**2 for i in range(n)]
return wynik


def hello():
    print("Hello")
    #rerurn None to dziala domyslnie

def sumuj(a,b):
    print(a, b)
    return a + b

n2 = kwadraty(2)
n3 = kwadraty(3)
n10 = kwadraty(10)

print(n2)
print(n3)
print(n10)

h =hello()
print(h)
# suma = sumuj(b=10, a=20)
# print(suma)

def incr_a():
    a = a + 1
icr_a()
print("a", a)