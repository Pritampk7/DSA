def containsduplicate(arr):
    hashset = set()
    for item in arr:
        if item in hashset:
            return True
        else:
            hashset.add(item)
    return False


arr = [1, 2, 2, 4]
print(containsduplicate(arr))
