def findmax(*args):
    if type(args[0]) == list:
        big = args[0]
        maxsum = big[0]
        for i in range(1, len(big)):
            if big[i] > maxsum:
                maxsum = big[i]
        return maxsum

    elif type(args) == tuple or set:
        maxsum = args[0]
        for i in range(1, len(list(args))):
            if args[i] > maxsum:
                maxsum = args[i]
        return maxsum


def maxproduct(arr):
    res = findmax(arr)
    curmin, curmax = 1, 1
    for item in arr:
        tmp = curmax * item
        curmax = findmax(curmin * item, curmax * item, item)
        curmin = findmax(curmin * item, tmp, item)
        res = findmax(curmax, res, curmin)
    return res


print(maxproduct([2, 1, -2, 3]))
