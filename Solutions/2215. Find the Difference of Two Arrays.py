# 2215. Find the Difference of Two Arrays
# Quick and bad decision
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in answer[0]:
                answer[0].append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in answer[1]:
                answer[1].append(nums2[i])
        return answer
