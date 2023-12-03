class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for p in s.split(' '):
            res += p[::-1]
            res += " "
        res = res[:-1]
        return res