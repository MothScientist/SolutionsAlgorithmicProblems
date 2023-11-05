# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and set(s) == set(t):
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
            return True
        return False