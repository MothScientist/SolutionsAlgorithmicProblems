# 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left_profits = [0] * len(prices)
        right_profits = [0] * len(prices)

        # Calculate the maximum profit from left to right
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i-1], prices[i] - min_price)

        # Calculate the maximum profit from right to left
        max_price = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profits[i] = max(right_profits[i+1], max_price - prices[i])

        max_profit = max(map(sum, zip(left_profits, right_profits)))

        return max_profit

# 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        if max(prices) == 0: return 0

        buy_1, buy_2 = 10**5 + 1, 10**5 + 1
        sell_1, sell_2 = 0, 0

        for i in range(len(prices)):
            buy_1 = min(buy_1, prices[i])
            sell_1 = max(sell_1, prices[i] - buy_1)

            buy_2 = min(buy_2, prices[i] - sell_1)
            # The value will decrease when:
            # - increasing income from the first transaction
            # - reducing the purchase price of the second share
            sell_2 = max(sell_2, prices[i] - buy_2)
            # - (- sell_1) = sell_1
            # therefore, the income from the first sale will be added here
        return sell_2