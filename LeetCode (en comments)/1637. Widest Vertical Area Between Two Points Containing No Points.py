class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        # points[i][0] contains the x coordinate

        # since the region cannot have points inside, 
        # you just need to look for the difference in the x coordinate between each group of points

        # group of points - points that have equal x coordinates

        res = -1

        for j in range(1, len(points)):
            res = max(res, points[j][0] - points[j-1][0])
        return res