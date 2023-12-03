class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)-1):
            if prices[i] >= min(prices[i + 1:]):
                for j in range(1, len(prices) - i):
                    if prices[i] >= prices[i + j]:
                        prices[i] = prices[i] - prices[i + j]
                        break
        return prices