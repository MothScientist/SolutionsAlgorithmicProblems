class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        var = 0
        for i in range(len(mat)):
            var += mat[i][i]
            var += mat[i][len(mat) - 1 - i]
            if i == len(mat) - 1 - i:
                var -= mat[i][i]
        return var

