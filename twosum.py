arr = [2, 7, 11, 15]
target = 9


def twosum(arr, target):
    values = {}  # value:index
    for index, value in enumerate(arr):
        diff = target - value
        if diff in values:
            return values[diff], index
        values[value] = index


print(twosum(arr, target))
