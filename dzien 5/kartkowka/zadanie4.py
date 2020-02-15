
def double_letters(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True
    return False





def test_double_letters():
    assert double_letters("ala") == False
    assert double_letters("Hello") == True
    assert double_letters("abc") == False