import math
# find the center of the 2D matrix
    # find the highest square if even rows/cols
    # arr[row][col] to locate square


def find_start_square(arr):
    rows = len(arr)
    cols = len(arr[0])

    row = math.ceil(rows / 2)
    col = math.ceil(cols / 2)

    return row, col


def find_next_square(arr, row, col):
    largest_val = 0
    largest_row = None
    largest_col = None

    if row > 0 and arr[row - 1][col] > largest_val:
        largest_val = arr[row - 1][col]
        largest_row = row - 1
        largest_col = col

    if len(arr) - 1 > row and arr[row + 1][col] > largest_val:
        largest_val = arr[row + 1][col]
        largest_row = row + 1
        largest_col = col

    if col > 0 and arr[row][col - 1] > largest_val:
        largest_val = arr[row][col - 1]
        largest_row = row
        largest_col = col - 1

    if len(arr[0]) - 1 > col and arr[row][col + 1] > largest_val:
        largest_val = arr[row][col + 1]
        largest_row = row
        largest_col = col + 1

    return largest_row, largest_col


def move_through_array(arr):
    item_count = 0

    row, col = find_start_square(arr)

    while True:
        items = arr[row][col]
        item_count += items
        row, col = find_next_square(arr, row, col)
        if row is None or col is None:
            break

    return item_count
