# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        max_h = h
        for i in gain:
            h += i
            max_h = max(max_h, h)
        return max_h