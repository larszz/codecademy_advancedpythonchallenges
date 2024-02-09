def get_blocking_diagonal_field(spot1: int, spot2: int) -> int | None:
    diagonals = [[0, 4, 8], [2, 4, 6]]
    for d in diagonals:
        try:
            d.remove(spot1)
            d.remove(spot2)
            if len(d) == 1:
                return d[0]
        except ValueError:
            pass
    return None


def get_blocking_line_field(spot1: int, spot2: int) -> int | None:
    for line in [0, 3, 6]:
        line_spots = [_ for _ in range(line, line + 3)]
        try:
            line_spots.remove(spot1)
            line_spots.remove(spot2)
            if len(line_spots) == 1:
                return line_spots[0]
        except ValueError:
            pass
    return None


def get_blocking_row_field(spot1: int, spot2: int) -> int | None:
    for row in range(0, 3):
        row_spots = [row + 3 * line for line in range(0, 3)]
        try:
            row_spots.remove(spot1)
            row_spots.remove(spot2)
            if len(row_spots) == 1:
                return row_spots[0]
        except ValueError:
            pass
    return None


def get_blocking_field(spot1: int, spot2: int) -> int:
    blocking_diagonal = get_blocking_diagonal_field(spot1, spot2)
    if blocking_diagonal:
        return blocking_diagonal

    blocking_line = get_blocking_line_field(spot1, spot2)
    if blocking_line:
        return blocking_line

    blocking_row = get_blocking_row_field(spot1, spot2)
    if blocking_row:
        return blocking_row

    raise Exception(f"No blocking field found for spots {spot1} and {spot2}")


"""
0   1   2
3   4   5
6   7   8
"""

if __name__ == '__main__':
    print(str(get_blocking_field(0, 1)))
    print(str(get_blocking_field(0, 3)))
    print(str(get_blocking_field(0, 2)))
    print(str(get_blocking_field(0, 4)))
    print(str(get_blocking_field(0, 8)))
    print(str(get_blocking_field(6, 4)))
    # print(str(get_blocking_field(6, 1)))
