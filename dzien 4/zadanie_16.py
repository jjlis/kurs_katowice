# Napisz funkcje ktora zwroci dlugosc najdluzszego ciagu tego samego znaku w napisie
# np: consecutive("aabbbaabbbb", "b") -> 4


def consecutive(tekst, sign):
    longest_counter = 0
    counter = 0
    for s in tekst:
        if s == sign:
            counter += 1
        else:
            longest_counter = max(counter, longest_counter)
            counter = 0
    longest_counter = max(counter, longest_counter)
    return longest_counter


def test_consecutive():
    assert consecutive("aabbbaabbbb", "b") == 4
    assert consecutive("aabbbaabbbb", "a") == 2
    assert consecutive("aabbbbaabbb", "a") == 4
