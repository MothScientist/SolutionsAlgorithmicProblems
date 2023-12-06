class Solution:
    def totalMoney(self, n: int) -> int:
        full_week = n // 7
        n = n % 7
        res = 0

        if full_week:
            for i in range(full_week):
                res += 28 + (7 * i)

        if n:
            for j in range(1, n+1):
                res += j + full_week

        return res