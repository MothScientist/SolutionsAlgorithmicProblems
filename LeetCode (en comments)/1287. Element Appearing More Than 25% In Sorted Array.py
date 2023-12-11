#1 (the fastest)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        window = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + window]:
                return arr[i]

#2
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = 0
        for i in arr:
            if arr.count(i) > len(arr) // 4:
                return i

#3
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = 0
        count = 0
        for i in arr:
            if arr.count(i) > count:
                count = arr.count(i)
                res = i
        return res