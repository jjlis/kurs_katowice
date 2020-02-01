# Napisz 2 funkcje
#add_dots
#remove_dots
#przyjmą one napis jako parametr. Pierwsza z nich ma wstawic kropki pomiedzy znaki, np add_dots('text') -> t.e.x.t
#druga odwrotnie:
#remove_dots('t.e.x.t') -> text

def add_dots(text):
    return".".join(param))



def test_add_dots():
    assert test_add_dots("text") == "t.e.x.t"

def remove_dots():
   # return "".join(param.split("."))::
    return param.replae(".","")

def test_remove_dots():
    assert remove_dots("t.e.x.t") == "text"