class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = dict()
        for i in set(arr):
            res.update({i: arr.count(i)})
        if len(list(res.values())) == len(set(res.values())):
            return True
        return False