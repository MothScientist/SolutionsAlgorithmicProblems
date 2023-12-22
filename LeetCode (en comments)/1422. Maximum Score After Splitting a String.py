class Solution:
    def maxScore(self, s: str) -> int:
        res = -1
        count_zeros_before = 0
        count_ones_after = 0

        for i in s:
            if i == "1":
                count_ones_after += 1

        for j in range(len(s) - 1):
            if s[j] == "1":
                count_ones_after -= 1
            else:
                count_zeros_before += 1
            res = max(res, count_zeros_before + count_ones_after)
            
        return res