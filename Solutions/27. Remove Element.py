# 27. Remove Element

# 1.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
# 2.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        while val in nums:
            nums.pop(nums.index(val))
            nums.append('_')
            res += 1
        return len(nums) - res