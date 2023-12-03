# 1356. Sort Integers by The Number of 1 Bits
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def hammingWeight(n: int) -> int:
            count = 0
            for i in range(0, 33):
                if n & 1 << i != 0:
                    count += 1
            return count, n

        arr.sort(key = hammingWeight)
        return arr