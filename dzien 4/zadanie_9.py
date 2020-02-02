# Dwa napisy sa anagramami jesli mozna z liter jednego poprzez ich przestawienie zrobic drugi.
# Napisz funckje: is_anagram, ktora przyjmie dwa napisy i sprawdzi czy sa anagramami.

# sprawdzenie typowania-dnotacje.
def is_anagram(a: str, b: str) -> bool:
    """
    Sprawdza czy dwa napisy to anagramy
    :param a: 
    :param b: 
    :return: 
    """"""
   
return sorted(a.lower()) == sorted(b.lower())


#bez funkcji:
# a = "Tokio"
# b = "Kioto"
# a = a.lower()
# b = b.lower()
#print (sorted(a))
#print(sorted(b))
#print(sorted(a) == sorted(b))

def test_is_anagram():
    assert is_anagram("Tokio", "Kioto") == True
    assert is_anagram ("Anna", "Bob") == False
