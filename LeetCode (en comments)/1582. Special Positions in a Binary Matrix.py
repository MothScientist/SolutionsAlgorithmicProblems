class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        res = 0

        def get_column_sum(column):
            return sum(_row_[column] for _row_ in mat)

        for row in range(rows):
            if sum(mat[row]) == 1 and get_column_sum(mat[row].index(1)) == 1:
                res += 1
        
        return res