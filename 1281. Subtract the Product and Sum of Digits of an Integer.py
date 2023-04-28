# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digit, product = 0, 1
        for i in str(n):
            sum_digit += int(i)
            product *= int(i)
        return product - sum_digit