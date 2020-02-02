# def incr(a):
#     print(a)
#     incr(a+1)
#
# incr(10)

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

print(silnia)

def test_silnia():
    assert silnia(4) == 24
    assert silnia(5) == 120