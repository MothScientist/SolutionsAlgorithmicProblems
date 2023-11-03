# 566. Reshape the Matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:  # check if we can create a new matrix
            return mat

        flatten  = []
        for x in mat:
            flatten .extend(x if isinstance(x, list) else [x])

        mat = [[0 for _ in range(c)] for _ in range(r)]  # to save memory, we transform the existing list

        k = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = flatten [k]
                k += 1

        return mat