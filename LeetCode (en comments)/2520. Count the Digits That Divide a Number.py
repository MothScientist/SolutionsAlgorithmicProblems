class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for i in str(num):
            if num % int(i) == 0:
                res += 1
        return res