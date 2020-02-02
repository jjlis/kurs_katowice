# Mamy plansze do gry w kolko i krzyzyk
# 1:  x | o | x
# 2:    |   |
# 3:  O |   |
#     A   B   C

# board = [["X", "O", "X"],
#          [" ", " ", " "],
#          ["o", " ", " "],
# ]
# Napisz funkcje get_row_col
#ktora przyjmie napis odpowiadajacy polozeniu na planszy np A1, C2, i zwroci koordynaty
# get_row_col("A3") -> (2,0)

def get_row_col(position):
    columns = "ABC"
    rows = "123"
    col_n, row_n = list(position)
    try:
        return rows.index(row_n), columns.index(col_n)
    except:
        return "Koordynata spoza planszy"


def test_get_row_col():
    assert get_row_col("A3") == (2,0)
    assert get_row_col("C3") == (2,2)