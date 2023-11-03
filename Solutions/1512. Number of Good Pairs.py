# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        scr = 0
        nums = [i for i in nums if nums.count(i) > 1]
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] == nums[j]:
                    scr += 1
        return scr