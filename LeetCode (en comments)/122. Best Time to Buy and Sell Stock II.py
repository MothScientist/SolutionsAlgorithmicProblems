class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # we want to record in the dp list how much the stock has risen and fill it with zeros if it has fallen
        dp = [0] * (len(prices) - 1)

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            dp[i - 1] = diff if diff >=0 else 0

        return sum(dp)