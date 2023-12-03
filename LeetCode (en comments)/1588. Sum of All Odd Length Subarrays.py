class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
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