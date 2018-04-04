# Given listing of store hours, represent the data in memory, write a function
# to parse the data, and write a function given_time to return whether the store
# is open at a given time


def parse_store_hours(hours_file):
    """Read store hours from file and return dictionary of store hours."""

    store_hours = {}

    with open(hours_file, 'r') as f:
        for line in f:
            entry = line.rstrip()

            day, hours = entry.split(':')
            start_str, end_str = hours.split(' to ')

            start = int(start_str[:-2])
            end = int(end_str[:-2]) + 12

            store_hours[day.lower()] = (start, end)

    return store_hours


def is_open(day, time):
    """Returns whether store is open at given time.

    Assumes time is given in 3:45pm format.

    >>> is_open('Monday', '3:45pm')
    True
    >>> is_open('Tuesday', '1:22am')
    False

    """

    store_hours = parse_store_hours('store_hours.txt')

    day = day.lower()
    is_morning = True

    if time[-2] == 'p':
        is_morning = False

    time = time[:-2]
    hour_str, min_str = time.split(':')
    hour = int(hour_str)
    minute = int(min_str)

    if not is_morning:
        hour += 12

    time_value = hour + (minute // 60)

    if store_hours[day][0] <= time_value and time_value <= store_hours[day][1]:
        return True

    return False
