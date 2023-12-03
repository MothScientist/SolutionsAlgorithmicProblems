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
