# 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        if len(nums) == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])

        dp = [0 for i in range(len(nums)-1)]
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        temp = dp[-1]

        nums = nums[1:]
        dp = [0 for i in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(temp, dp[-1])