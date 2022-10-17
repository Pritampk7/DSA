arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxsumofthesubarray(arr):

    maxsum = arr[0]
    temp_sum = 0

    for item in arr:
        if temp_sum < 0:
            temp_sum = 0
        temp_sum += item
        maxsum = max(maxsum, temp_sum)

    return maxsum


print(maxsumofthesubarray(arr))