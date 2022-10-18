
def findmin(arr):
    res = arr[0]
    l, r = 0, len(arr) - 1
    while l <= r:
        if arr[l] < arr[r]:
            res = min(res, arr[l])
            return res
        mid = (l + r) // 2
        res = min(res, arr[mid])
        if arr[mid] >= arr[l]:
            l = mid + 1
        else:
            r = mid - 1
    return res


arr = [1, 5, 7, 6, 5, 2]
print(findmin(arr))
