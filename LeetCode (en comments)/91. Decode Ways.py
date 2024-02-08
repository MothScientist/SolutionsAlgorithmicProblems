class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or not s:
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        # valid string won`t start from zero
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):  # array dp is 1 larger than string s
            # For single digit number
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # For two-digit number
            if 10 <= int(s[i-2:i]) <= 26:
                # if we take 2 numbers, it means that we no longer take the previous number into account as a single number, 
                # so we add the result that was 1 step ago
                dp[i] += dp[i-2]
        return dp[-1]