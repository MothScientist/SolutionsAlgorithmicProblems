# 202. Happy Number
# LeetCode Easy
#
#
#
#Write an algorithm to determine if a number n is happy.
#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), 
#or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.

#Example 1:
#Input: n = 19
#Output: true
#Explanation:
#1**2 + 9**2 = 82
#8**2 + 2**2 = 68
#6**2 + 8**2 = 100
#1**2 + 0**2 + 02 = 1

#Example 2:
#Input: n = 2
#Output: false

def isHappy(self, n: int) -> bool:
        while n != 1:
            new_digit = 0
            for i in str(n):
                new_digit += int(i)**2
            n = new_digit
            if n == 4:
                return False
        return True