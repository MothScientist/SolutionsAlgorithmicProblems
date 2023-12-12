# 1
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1 = max(nums)
        nums.remove(max_1)
        max_2 = max(nums)
        return (max_1 - 1) * (max_2 - 1)

# 2
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

# 3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = -1
        second_largest = -1
        for i in nums:
            if i > second_largest:
                second_largest = i
            if second_largest > largest:
                second_largest, largest = largest, second_largest
        return (largest - 1) * (second_largest - 1)