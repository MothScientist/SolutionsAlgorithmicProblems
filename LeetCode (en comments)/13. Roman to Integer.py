class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        diff = d.get(s[0])
        for i in range(1, len(s)):
            if d.get(s[i]) == d.get(s[i-1]):
                diff += d.get(s[i])
            elif d.get(s[i]) > d.get(s[i-1]):
                res += d.get(s[i]) - diff
                diff = 0
            elif d.get(s[i]) < d.get(s[i-1]):
                res += diff
                diff = d.get(s[i])
        res += diff
        return res