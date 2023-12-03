class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        scr = []
        m = len(arr[0])
        n = len(arr)
        top, bottom, left, right = 0, n - 1, 0, m - 1

        while len(scr) < n*m:

            for i in range(left, right + 1):
                scr.append(arr[top][i])
            top += 1

            for j in range(top, bottom + 1):
                scr.append(arr[j][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    scr.append(arr[bottom][i])
                bottom -= 1

            if left <= right:
                for j in range(bottom, top - 1, -1):
                    scr.append(arr[j][left])
                left += 1

        return scr