class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a1 = ''.join(i for i in word1)
        a2 = ''.join(j for j in word2)
        if a1 == a2:
            return True
        return False


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if ''.join(word1) == ''.join(word2):
            return True
        return False