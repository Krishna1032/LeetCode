class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        if prices == sorted(prices, reverse=True):
            return 0

        if prices == sorted(prices):
            return max(prices) - min(prices)

        min_value_index = prices.index(min(prices))
        while min_value_index == len(prices) - 1 and len(prices) != 1:
            prices.pop(min_value_index)
            min_value_index = prices.index(min(prices))

        if len(prices) == 1:
            return 0

        profit = 0
        current = 10e4 + 1
        prev_current = -2
        for i in range(len(prices)):
            current = prices[i] if current > prices[i] else current
            if current == prev_current:
                continue
            difference = max(prices[i + 1 :]) - current
            if difference >= profit:
                profit = difference
            prev_current = current
        return profit
