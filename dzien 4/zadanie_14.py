"""
Napisz funkcje, ktora sprawdzi, czy tekst jest palindromem, tzn czy czytany wspak jest taki sa jak czytany od poczatku.
Zacznij od prostych: ola, kajak, a potem sprobuj ze spacjami, przecinkami ttd..
palindrome("kajak") -> True
palindrome("Kajak") -> True
palindrome ("A to idiota") -> True
"""
import string # weszlam sobie do innego pliku o strngach

def palindrome(tekst):
    to_replace = ",.-!"
    tekst = tekst.lower()
    for s in string.punctuation + string.whitespace:
        tekst = tekst.replace(s, "")
    return tekst == tekst [::-1]



def test_palindrome():
    assert palindrome("kajak") is True
    assert palindrome("Kajak") is True
    assert palindrome("A to idiota") is True
