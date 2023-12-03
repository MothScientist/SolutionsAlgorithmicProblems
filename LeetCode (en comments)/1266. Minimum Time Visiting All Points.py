class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points)-1):
            cur_x = points[i][0]
            cur_y = points[i][1]
            next_x = points[i+1][0]
            next_y = points[i+1][1]
            
            dif_x = abs(next_x - cur_x)
            dif_y = abs(next_y - cur_y)

            steps += max(dif_y, dif_x)
        return steps