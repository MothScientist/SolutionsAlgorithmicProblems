# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        res = s[0]

        for i in range(len(res)):
            for j in s[1:]:
                if i == len(j) or j[i] != res[i]:
                    return res[:i]

        return res
