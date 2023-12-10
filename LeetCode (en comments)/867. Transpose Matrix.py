class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        len_row = len(matrix)
        len_column = len(matrix[0])
        res = [[0] * len_row for _ in range(len_column)]

        for i in range(len_column):
            for j in range(len_row):
                res[i][j] = matrix[j][i]

        return res