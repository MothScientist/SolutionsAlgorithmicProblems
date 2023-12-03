import unittest
# 1588. Sum of All Odd Length Sub-arrays
# LeetCode Easy
#
#
#
# Given an array of positive integers arr, return the sum of all possible odd-length sub-arrays of arr.
# A subarray is a contiguous subsequence of the array.
#
# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
#
# Example 2:
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 sub-arrays of odd length, [1] and [2]. Their sum is 3.
#
# Example 3:
# Input: arr = [10,11,12]
# Output: 66


class SquareEqSolverTestCase(unittest.TestCase):

    def test_0(self):
        res = sum_odd_length_sub_arrays([1, 4, 2, 5, 3])
        self.assertEqual(res, 58)

    def test_1(self):
        res = sum_odd_length_sub_arrays([1, 2])
        self.assertEqual(res, 3)

    def test_2(self):
        res = sum_odd_length_sub_arrays([10, 11, 12])
        self.assertEqual(res, 66)

    def test_3(self):
        res = sum_odd_length_sub_arrays([1])
        self.assertEqual(res, 1)

    def test_4(self):
        res = sum_odd_length_sub_arrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(res, 2752)

    def test_5(self):
        res = sum_odd_length_sub_arrays([100, 203, 234, 235, 235, 426, 245, 967])
        self.assertEqual(res, 18044)


def sum_odd_length_sub_arrays(arr: list[int]) -> int:
    if len(arr) >= 3:
        var = sum(arr)
        len_carriage = 3
    else:
        return sum(arr)

    while len_carriage <= len(arr):

        for i in range(len(arr) - len_carriage + 1):
            var += sum(arr[i:len_carriage+i])

        len_carriage += 2
    return var


if __name__ == '__main__':
    unittest.main()
