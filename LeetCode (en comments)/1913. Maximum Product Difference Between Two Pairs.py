# 1
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        _max = [0, 0]
        _min = [10**4 + 1, 10**4 + 1]

        for i in nums:
            if i > min(_max):
                if _max[0] >= _max[1]:
                    _max[1] = i
                else:
                    _max[0] = i
            if i < max(_min):
                if _min[0] >= _min[1]:
                    _min[0] = i
                else:
                    _min[1] = i

        return _max[0] * _max[1] - _min[0] * _min[1]

# 2
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]