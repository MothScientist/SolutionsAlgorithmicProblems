# Time Limit Exceeded
# def replace_elements(arr: list[int]) -> list[int]:
#     return [max(arr[i:]) for i in range(1, len(arr))] + [-1]


# Time Limit Exceeded
# def replace_elements(arr: list[int]) -> list[int]:
#     return list(reversed([-1] + [max(arr[len(arr) - i:]) for i in range(1, len(arr))]))


# Time Limit Exceeded
# def replace_elements(arr: list[int]) -> list[int]:
#     answer = []
#     for i in range(1, len(arr)):
#         answer.insert(0, max(arr[len(arr) - i:]))
#     answer.append(-1)
#     return answer


# Accepted
def replace_elements(arr: list[int]) -> list[int]:
    curr_max = arr[-1]
    arr[-1] = -1
    for i in range(len(arr)-2,-1,-1):
        curr = arr[i]
        arr[i] = curr_max
        if curr > curr_max:
            curr_max = curr
    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
