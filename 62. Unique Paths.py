# 62. Unique Paths

# iterative method
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
        
# recursive method (Time Limit Exceeded, but the algorithm works correctly)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = 0
        def paths(m, n, x, y):
            if x == m - 1 and y == n - 1:
                nonlocal path
                path += 1
            else:
                if x == m - 1 and y < n - 1:
                    paths(m, n, x, y + 1)
                elif x < m - 1 and y == n - 1:
                    paths(m, n, x + 1, y)
                else:
                    paths(m, n, x, y + 1)
                    paths(m, n, x + 1, y)
        paths(m, n, 0, 0)
        return path