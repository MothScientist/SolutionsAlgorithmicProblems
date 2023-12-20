class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        s = sum(prices[:2])
        if s > money:
            return money
        return money - s