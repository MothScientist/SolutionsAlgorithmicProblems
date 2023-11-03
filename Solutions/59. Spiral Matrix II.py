# 59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[i for i in range(n)] for j in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        arg = 1
        while arg <= n**2:

            for i in range(left, right + 1):
                arr[top][i] = arg
                arg += 1
            top += 1

            for j in range(top, bottom + 1):
                arr[j][right] = arg
                arg += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    arr[bottom][i] = arg
                    arg += 1
                bottom -= 1

            if left <= right:
                for j in range(bottom, top - 1, -1):
                    arr[j][left] = arg
                    arg += 1
                left += 1

        return arr