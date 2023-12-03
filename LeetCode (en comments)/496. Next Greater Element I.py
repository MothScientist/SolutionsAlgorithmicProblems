# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        # 496. Next Greater Element I
        # All integers in nums1 and nums2 are unique!
        # All the integers of nums1 also appear in nums2.
        for i in nums1:
            answer.append(-1)
            for j in nums2[nums2.index(i) + 1:]:
                if j > i:
                    answer[-1] = j
                    break
        return answer
