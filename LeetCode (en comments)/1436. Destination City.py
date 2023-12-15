class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        right_set: set = set()
        left_set: set = set()

        for path in paths:
            right_set.add(path[-1])
            left_set.add(path[0])

        return right_set.difference(left_set).pop()  # or (right_set - left_set).pop()