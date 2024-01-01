# 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = int((n/2) * (1 + n))
        return s - sum(nums)

# 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_numbers = [i for i in range(len(nums) + 1)]
        return sum(all_numbers) - sum(nums)

# 3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_numbers = {i for i in range(len(nums) + 1)}
        return all_numbers.difference(nums).pop()