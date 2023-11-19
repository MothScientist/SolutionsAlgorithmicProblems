class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        counter = 0
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
            else:
                ind = stack.index(s[i])
                stack = stack[ind+1:]
                stack.append(s[i])

            if len(stack) > counter:
                    counter = len(stack)
        return counter