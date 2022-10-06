prices = [7, 1, 2, 4, 6, 7]


def stockbuyandsell(prices):
    buy = 0
    sell = 1
    maxprofit = 0

    for i in range(len(prices) - 1):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
        else:
            buy = sell
        sell += 1

    return maxprofit


print(stockbuyandsell(prices))
