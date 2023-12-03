import unittest


# LeetCode Easy
# 13. Roman to Integer
#
#
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol Value:
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
# which is simply X + II.The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.However, the numeral for four is not IIII.
# Instead,  the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V(5) and X(10) to make 4 and 9. X can be placed before L(50) and C(100) to make 40 and 90.
# C can be placed before D(500) and M(1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
# Constraints:
#
# 1 <= s.length <= 15
# s contains only the characters('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range[1, 3999].


class SquareEqSolverTestCase(unittest.TestCase):

    def test_III(self):
        res = roman_to_int("III")
        self.assertEqual(res, 3)

    def test_LVIII(self):
        res = roman_to_int("LVIII")
        self.assertEqual(res, 58)

    def test_MCMXCIV(self):
        res = roman_to_int("MCMXCIV")
        self.assertEqual(res, 1994)

    def test_MMMDIX(self):
        res = roman_to_int("MMMDIX")
        self.assertEqual(res, 3509)

    def test_DLXXVI(self):
        res = roman_to_int("DLXXVI")
        self.assertEqual(res, 576)

    def test_CCCXLVI(self):
        res = roman_to_int("CCCXLVI")
        self.assertEqual(res, 346)

    def test_CI(self):
        res = roman_to_int("CI")
        self.assertEqual(res, 101)

    def test_LXXXIX(self):
        res = roman_to_int("LXXXIX")
        self.assertEqual(res, 89)

    def test_DCCXCIX(self):
        res = roman_to_int("DCCXCIX")
        self.assertEqual(res, 799)

    def test_XXXV(self):
        res = roman_to_int("XXXV")
        self.assertEqual(res, 35)

    def test_CMLII(self):
        res = roman_to_int("CMLII")
        self.assertEqual(res, 952)

    def test_DCXLVIII(self):
        res = roman_to_int("DCXLVIII")
        self.assertEqual(res, 648)

    def test_MMMDCCLIV(self):
        res = roman_to_int("MMMDCCLIV")
        self.assertEqual(res, 3754)

    def test_MMCCCLVI(self):
        res = roman_to_int("MMCCCLVI")
        self.assertEqual(res, 2356)

    def test_I(self):
        res = roman_to_int("I")
        self.assertEqual(res, 1)

    def test_MMMCMXCIX(self):
        res = roman_to_int("MMMCMXCIX")
        self.assertEqual(res, 3999)

    def test_MMMDCCCLXVII(self):
        res = roman_to_int("MMMDCCCLXVII")
        self.assertEqual(res, 3867)

    def test_MMMCM(self):
        res = roman_to_int("MMMCM")
        self.assertEqual(res, 3900)


def roman_to_int(s: str):
    math = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    answer = 0
    digit = math.get(s[0])
    for i in range(1, len(s)):
        if math.get(s[i]) == math.get(s[i - 1]):
            digit += math.get(s[i - 1])
        else:
            digit += math.get(s[i])
            if math.get(s[i]) > math.get(s[i - 1]):
                answer += 2*math.get(s[i]) - digit
                digit = 0
            else:
                answer += digit - math.get(s[i])
                digit = math.get(s[i])
    answer += digit
    return answer


if __name__ == '__main__':
    unittest.main()
