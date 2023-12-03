# 2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        num1 = [sum(nums[i:]) for i in range(1, len(nums))] + [0]
        num2 = [0] + [sum(nums[:i]) for i in range(1, len(nums))]
        res = []
        for i in range(len(nums)):
            res.append(abs(num1[i] - num2[i]))
        return res