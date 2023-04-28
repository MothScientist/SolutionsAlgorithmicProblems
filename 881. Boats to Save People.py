# LeetCode Medium
#
#
#
# You are given an array people where people[i] is
# the weight of the ith person, and an infinite number
# of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
def num_rescue_boats(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        boats += 1
    return boats


print(num_rescue_boats([3, 5, 3, 4], 5))
