class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = len(words)
        for s in words:
            for i in s:
                if i not in allowed:
                    res -= 1
                    break
        return res