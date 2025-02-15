class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        l = len(s)
        for i in range(len(s) // 2):
            if s[i] != s[l - 1 - i]:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]