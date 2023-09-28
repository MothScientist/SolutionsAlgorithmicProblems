class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in nums:
            if i % 2 == 0:
                arr1.append(i)
            else:
                arr2.append(i)

        arr1.sort()
        arr2.sort()
        return arr1+arr2