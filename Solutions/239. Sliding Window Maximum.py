# 239. Sliding Window Maximum

# Why collections.deque?

# Though list objects support similar operations, 
# they are optimized for fast fixed-length operations 
# and incur O(n) memory movement costs for pop(0) 
# and insert(0, v) operations which change both the size 
# and position of the underlying data representation.

# Accepted:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        for i in range(len(nums)):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res

# Time Limit:
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         for i in range(0, len(nums)-k+1):
#             nums[i] = max(nums[i:k+i])
#         return nums[:len(nums)-k+1]