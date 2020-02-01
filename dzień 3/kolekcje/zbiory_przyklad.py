# suma |
# roznica -

set()

print(set([1, 2, 3]))

print(set([1, 1, 1, 2, "a"]))
x = set("abcba")
for i in x:
    print(i)

x.add("d")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A - B)
print(A & B) # czesc wspolna
print(A ^ B) #roznica symetryczna