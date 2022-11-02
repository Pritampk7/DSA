def validAnagram(istring, ostring):

    inputHash, outputHash = {}, {}

    if len(istring) != len(ostring):
        return False
    for i in range(len(istring)):
        inputHash[istring[i]] = 1 + inputHash.get(istring[i], 0)
        outputHash[ostring[i]] = 1 + outputHash.get(ostring[i], 0)

    for count in inputHash:
        if inputHash[count] != outputHash.get(count, 0):
            return False
    return True

print(validAnagram("data", "data"))
