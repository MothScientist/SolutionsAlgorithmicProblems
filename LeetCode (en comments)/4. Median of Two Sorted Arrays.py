class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr3 = nums1 + nums2
        arr3.sort()
        len3 = len(arr3)

        if len3 % 2 != 0:
            return arr3[len3//2]
        return arr3[len3//2-1] / 2.0 + arr3[len3//2] / 2.0