# 1
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ways = dict()
        max_len = -1

        for i in range(len(s)):
            if s[i] not in ways:
                ways[s[i]] = i
            else:
                way = ways.get(s[i])
                max_len = max(i - way - 1, max_len)

        return max_len

# 2
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ways = dict()
        score = []

        for i in range(len(s)):
            if s[i] not in ways:
                ways[s[i]] = i
            else:
                way = ways.get(s[i])
                score.append(i - way - 1)

        return max(score) if len(score) > 0 else -1