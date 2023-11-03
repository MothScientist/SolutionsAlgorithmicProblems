# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]