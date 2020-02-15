def is_anagram(a = str, b = str) -> bool:
    return sorted(a.lower()) == sorted(b.lower())



def test_is_anagram():
    assert is_anagram("typhoon", "opython") == True
    assert is_anagram("Alice", "Bob") == False