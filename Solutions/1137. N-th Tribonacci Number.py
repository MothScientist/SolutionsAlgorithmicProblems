# 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}
        if n in cache:
            return cache[n]
        def trib(k: int):
            if k in cache:
                return cache[k]
            cache[k] = trib(k-1) + trib(k-2) + trib(k-3)
            return cache[k]
        return trib(n)