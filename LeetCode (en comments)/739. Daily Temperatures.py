class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(arr))]

        for i in range(len(arr)):
            while stack and stack[-1][0] < arr[i]:
                old_index = stack.pop()[1]
                res[old_index] = i - old_index
            stack.append([arr[i], i])
        return res