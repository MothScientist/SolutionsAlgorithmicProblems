# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        curr = 0
        for i in nums:
            for _ in nums:
                if _ < i:
                    curr += 1
            res.append(curr)
            curr = 0
        return res