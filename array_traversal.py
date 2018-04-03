

def find_start_square(arr):
    """Locate the square at the center of the array."""

    rows = len(arr)
    cols = len(arr[0])
    row = None
    col = None

    if rows % 2 != 0:
        row = int(rows / 2)
    else:
        top_ind, bottom_ind = int((rows / 2) - 1), int(rows / 2)

    if cols % 2 != 0:
        col = int(cols / 2)
    else:
        left_ind, right_ind = int((cols / 2) - 1), int(cols / 2)

    if row is None and col is None:
        largest_val = arr[top_ind][left_ind]
        row = top_ind
        col = left_ind

        if arr[bottom_ind][left_ind] > largest_val:
            largest_val = arr[bottom_ind][left_ind]
            row = bottom_ind
        if arr[top_ind][right_ind] > largest_val:
            largest_val = arr[top_ind][right_ind]
            row = top_ind
            col = right_ind
        if arr[bottom_ind][right_ind] > largest_val:
            row = bottom_ind
            col = right_ind

    if row is None:
        if arr[top_ind][col] > arr[bottom_ind][col]:
            row = top_ind
        else:
            row = bottom_ind

    if col is None:
        if arr[row][left_ind] > arr[row][right_ind]:
            col = left_ind
        else:
            col = right_ind

    return row, col


def find_next_square(arr, row, col):
    """Find the contiguous square with the largest value."""

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
    """Start at the center, move through the array until no more valid moves."""

    item_count = 0

    row, col = find_start_square(arr)

    while True:
        items = arr[row][col]
        item_count += items
        arr[row][col] = -1
        print(arr)

        row, col = find_next_square(arr, row, col)
        if row is None or col is None:
            break

    return item_count
