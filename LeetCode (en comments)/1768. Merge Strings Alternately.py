class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(min(len(word1), len(word2))):
            output += word1[i] + word2[i]
        if len(word1) != len(word2):
            output += max(word1[min(len(word1), len(word2)):], word2[min(len(word1), len(word2)):])
        return output