# 1
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = [[0,0]]
        x, y = 0,0
    
        for i in range(len(path)):
            x = paths[-1][0]
            y = paths[-1][1]

            if path[i] == "N":
                y += 1
            elif path[i] == "S":
                y -= 1
            elif path[i] == "E":
                x += 1
            else:
                x -= 1

            if [x,y] in paths:
                return True

            paths.append([x,y])

        return False

# 2
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = [[0,0]]
        location = list()
    
        for i in range(len(path)):
            """
            So that it does not refer to the paths list object, 
            but only copies its last element, 
            which is placed in a separate memory cell
            """
            location = paths[-1].copy()
            if path[i] == "N":
                location[1] += 1
            elif path[i] == "S":
                location[1] -= 1
            elif path[i] == "E":
                location[0] += 1
            else:
                location[0] -= 1

            if location in paths:
                return True

            paths.append(location)

        return False