def threesum(arr):
    arr.sort()
    res = []
    for index, value in enumerate(arr):
        if index > 0 and value == arr[index - 1]:
            continue
        l = index + 1
        r = len(arr) - 1
        while l < r:
            zerosum = value + arr[l] + arr[r]
            if zerosum > 0:
                r -= 1
            elif zerosum < 0:
                l += 1
            else:
                res.append([value, arr[l], arr[r]])
                l += 1
                while arr[l] == arr[l - 1]:
                    l += 1

    return res

print(threesum([-3, 3, 4, -3, 1, 2]))
