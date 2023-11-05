# 2413. Smallest Even Multiple

# brute force method
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(n, n*2+1):
            if i % n == 0 and i % 2 == 0:
                return i 

# more logical way
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n*2 if n % 2 != 0 else n
