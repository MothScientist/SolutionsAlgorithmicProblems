class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0  # see comment below
        dp = [0] * (len(prices) - 1)
        min_price = prices[0]  # the minimum price should be stored separately, since calling the min() function is too complicated for large lists
        for i in range(1, len(prices)):
            min_price = min_price if min_price <= prices[i] else prices[i]
            dp[i-1] = prices[i] - min_price  # dp[i - 1] because on prices[0] we have nothing to sell and we can only buy
        return max(dp) if max(dp) >= 0 else 0