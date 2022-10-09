class maxproduct:

    def getProduct(self, arr) -> int:
        current_sum = max(arr)
        currentMin, currentMax = 1, 1
        for item in arr:
            tmp = item * currentMax
            currentMax = max(item, item * currentMax, item * currentMin)
            currentMin = max(item, item * currentMin, tmp)
            current_sum = max(current_sum, currentMax)
        return current_sum


arr = [2, 3, -2, 4]
obj = maxproduct()
print(obj.getProduct(arr))
