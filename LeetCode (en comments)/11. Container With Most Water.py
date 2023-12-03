# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, area)

            # We move a lower plate in search of benefits for a more profitable one.
            if height[right] < height[left]: 
                right -= 1
            else:
                left += 1
                
        return max_area