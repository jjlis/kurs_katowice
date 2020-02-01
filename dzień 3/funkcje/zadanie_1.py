# Napisz funkcje o nazwie capitl_letters, ktora:
# przyjmie jeden argument-napis
# zwroci indeksy wielkich liter

#
# def capital_letters(text):
#     result = []
#     for i, letter in enumerate(text):  # numerowanie liter
#         if letter.isupper():
#             result.append(i)
# return result
#
#
# # Testy
# def test_capital_letters_all_small_letters():
#     assert capital_letters("hello") == []
#
#
# def test_capital_letters_small_and_big_letters():
#
#
#     assert capital_letters("HeLlO") == [0, 2, 4]  # test sprwdzajacy!


def mid (text):
    if len(text) % 2 ==)
        return ""
    return text[len(text)]

def test_mid_without_middle_letter():
    assert mid("aabbcc") == ""

def test_mid_with_middle_letter():
    assert mid("abc") == "b"
    assert mid("doremifasol") == "i"

def test_mid_empty_string():
    assert mid("") == "Pusty napis"