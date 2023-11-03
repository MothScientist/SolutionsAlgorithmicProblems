# 1779. Find Nearest Point That Has the Same X or Y Coordinate
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = 10000
        index = len(points)
        for i in points:
            if x == i[0] or y == i[1]:
                if abs(x - i[0]) + abs(y - i[1]) < dist:
                    dist = abs(x - i[0]) + abs(y - i[1])
                    index = points.index(i)
                elif abs(x - i[0]) + abs(y - i[1]) == dist and points.index(i) < index:
                    index = points.index(i)
        if index == len(points):
            return -1
        return index