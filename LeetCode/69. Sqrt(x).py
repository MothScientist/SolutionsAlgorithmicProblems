# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1.0
        while abs(s*s - x) >= 1e-2:
            s -= (s*s - x) / (2*s)
        return int(s)