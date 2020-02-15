def capital_letters(text):
    result = []
    for i, letter in enumerate(text):
        if letter.isupper():
            result.append(i)
    return result


def test_capital_letters():
    assert capital_letters("HeLlO") == [0, 2, 4]
