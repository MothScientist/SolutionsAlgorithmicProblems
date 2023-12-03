class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            new_digit = 0
            for i in str(n):
                new_digit += int(i)**2
            n = new_digit
            if n == 4:
                return False
        return True