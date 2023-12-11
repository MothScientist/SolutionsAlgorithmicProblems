# 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix)
        row = len(matrix[0])
        low = 0
        high = col * row - 1
        while low <= high:
            mid = (low + high) // 2
            mid_row = mid // row
            mid_col = mid % row
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

# 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in matrix:
            arr += i
        curr = arr[len(arr) // 2]
        while arr:
            curr = arr[len(arr) // 2]
            if curr < target:
                arr = arr[((len(arr) // 2) + 1):]
            elif curr == target:
                return True
            else:
                arr = arr[:((len(arr) // 2))]
        return False