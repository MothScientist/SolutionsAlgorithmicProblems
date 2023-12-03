class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for x in range(1, len(nums) + 1):
            if nums[len(nums) - x] == 0:
                nums.append(nums.pop(len(nums) - x))