def twosum2(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        sumNow = arr[left] + arr[right]
        if sumNow > target:
            right -= 1
        elif sumNow < target:
            left += 1
        else:
            return left + 1, right + 1


print(twosum2([1, 3, 5, 6, 9, 11], 10))
