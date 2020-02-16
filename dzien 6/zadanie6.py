

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x*other, self.y*other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise NotImplementedError()
    def __rmul__(self, other):
        return self.__mul__(other)
    @property
    def len(self):
        return math.sqrt(self.x)
    def __str__(self):
        return f"<Vector: {self.x}, {self.y}>"
class TestVector():
    def test_initialization(self):
        v = Vector(1, 2)
        assert v.x == 1
        assert v.y == 2
    def test_add(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert v1 + v2 == Vector(4, 6)
    def test_sub(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert v2 - v1 == Vector(2, 2)
    def test_mul_by_other_vector(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert v1 * v2 == 3 + 8
    def test_mul_by_scalar(self):
        v1 = Vector(1, 2)
        assert v1 * 2 == Vector(2, 4)
        assert 2 * v1 ==
    def test_mul_by_str(self):
        with pytest.raises(NotImplementedError):
            v1 * "1"