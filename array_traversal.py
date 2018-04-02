import math
# find the center of the 2D matrix
    # find the highest square if even rows/cols
    # garden[row][col] to locate square


def find_start_square(garden):
    rows = len(garden)
    cols = len(garden[0])

    row = math.ceil(rows / 2)
    col = math.ceil(cols / 2)

    return row, col


def find_next_square(garden, row, col):
    largest_val = 0
    largest_row = None
    largest_col = None

    if row > 0 and garden[row - 1][col] > largest_val:
        largest_val = garden[row - 1][col]
        largest_row = row - 1
        largest_col = col

    if len(garden) - 1 > row and garden[row + 1][col] > largest_val:
        largest_val = garden[row + 1][col]
        largest_row = row + 1
        largest_col = col

    if col > 0 and garden[row][col - 1] > largest_val:
        largest_val = garden[row][col - 1]
        largest_row = row
        largest_col = col - 1

    if len(garden[0]) - 1 > col and garden[row][col + 1] > largest_val:
        largest_val = garden[row][col + 1]
        largest_row = row
        largest_col = col + 1

    return largest_row, largest_col


def move_through_garden(garden):
    keep_moving = True
    carrot_count = 0

    row, col = find_start_square(garden)

    while keep_moving:
        carrots = garden[row][col]
        carrot_count += carrots
        row, col = find_next_square(garden, row, col)
        if row is None or col is None:
            break

    return carrot_count
