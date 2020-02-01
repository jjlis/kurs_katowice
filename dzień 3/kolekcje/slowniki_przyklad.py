x =[1,2]
#pary wartosci
# key:value
#rozdielane przecinkiem
#key-unikalna wartosc, hashowalna (najczesciej niemutowalna)
#value - to w zasadzie dowolny obiekt


pol_ang = {"kot":"cat",
           "pies": "dog",
           (1,2): "tupla",
           }
print(pol_ang)
pol_ang = dict(kot="cat", pies="dog")
print(pol_ang)
# pol_ang = dict([("kot", "cat")],("pies", "dog")])
# print(pol_ang)

# pol_ang["kaczka"] = "duck"
# print(pol_ang)
# pol_ang["kaczka"] = "a duck"
# print(pol_ang["cat"])
# if "jaszczurka" in pol_ang:
#     print(pol_ang["jaszczurka"])


print(pol_ang.get("jaszczurka"))
print(pol_ang.get("jaszczurka", "Brak hasła"))

print(dir(pol_ang)) # sprawdzam jakie sa inne opcje dla slownika

for k in pol_ang:
    print(k,pol_ang[k])

ilosci = { "k": 1000}
