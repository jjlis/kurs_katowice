
def only_inst(a, b):
    return type(a) == int and type(b) == int


def test_only_inst():
    assert only_inst(1, 2) == True
    assert only_inst(1, True) == False
    assert only_inst("a", 1) == False