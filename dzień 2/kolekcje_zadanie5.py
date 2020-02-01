#for i in range(10):
 #  print(i, end="   ")
#print()
#print()
#for i in range(10):
#    print(i, end="   ")
#    for j in range(10):
#        print(i*j,end="   ")


print("     ", end="")
for i in range(10):
    print(f'{i : 4}', end="")
print()
print()
for i in range(10):
    print(f"{i:<3}", end="")
    for j in range(10):
        print(f'{i * j:4}',end="   ")
print()