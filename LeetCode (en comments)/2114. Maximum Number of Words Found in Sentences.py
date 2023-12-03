class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for i in sentences:
            max_len = max(max_len, len(i.split()))
        return max_len