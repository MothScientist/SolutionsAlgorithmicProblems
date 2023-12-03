# 215. Kth Largest Element in an Array

# Time Limit Exceeded
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for _ in range(k-1):
            nums.remove(max(nums))
        return max(nums)

# Accepted
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot=random.choice(nums)

        left=[x for x in nums if x>pivot]
        mid=[x for x in nums if x==pivot]
        right=[x for x in nums if x<pivot]

        n=len(left)
        m=len(mid)
        
        if k<=n:
            return self.findKthLargest(left,k)

        elif k>(n+m):
            return self.findKthLargest(right,k-(n+m))

        else:
            return mid[0]  