class Solution:
    def sortArray(self, sorting_list: List[int]) -> List[int]:
        if len(sorting_list) < 2:
            return sorting_list
        elif len(sorting_list) == 2:
            if sorting_list[0] > sorting_list[1]:
                return [sorting_list[1], sorting_list[0]]
            else:
                return sorting_list
        left = self.sortArray(sorting_list[:len(sorting_list) // 2])
        right = self.sortArray(sorting_list[len(sorting_list) // 2:])
        li, ri = 0, 0
        result = []
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                result.append(left[li])
                li += 1
            elif right[ri] < left[li]:
                result.append(right[ri])
                ri += 1
            else:
                result.append(left[li])
                result.append(right[ri])
                li += 1
                ri += 1
        while li < len(left):
            result.append(left[li])
            li += 1
        while ri < len(right):
            result.append(right[ri])
            ri += 1
        return result