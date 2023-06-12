# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        l = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if l == nums[i-1]:
                    res.append(str(l))
                else:
                    res.append(str(l) + "->" + str(nums[i-1]))
                l = nums[i]

        if l == nums[-1]:
            res.append(str(l))
        else:
            res.append(str(l) + "->" + str(nums[-1]))
        return res