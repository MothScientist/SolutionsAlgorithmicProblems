# LeetCode Easy
# Not my solution

# Find slope for first two points, point1 and point2
# Then compare the slopes of all other points to this slope

def check_straight_line(coordinates: list[list[int]]) -> bool:
    (x1, y1), (x2, y2) = coordinates[0], coordinates[1]

    for x3, y3 in coordinates[2:]:
        if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
            return False

    return True
