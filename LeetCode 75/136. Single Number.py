# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        key = 0
        for i in nums:
            key = key ^ i
        return key