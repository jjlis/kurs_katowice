#Napisz funkcje double_letters, ktora bedzie analizowac napis i sprwdzac czy zawiera powtrzajace sie lietry. Jesli tak zwraca True jesli nie False.


def double_letters(text):
    for i in range(len(text)-1): #zeby doszedl do konca wyrazu a nie dalej
        if text[i] == text[i +1]:
            return True
    return False



def test_double_letters():
    assert double_letters("ala") == False
    assert double_letters("alla") == True
    assert double_letters("nono") == False