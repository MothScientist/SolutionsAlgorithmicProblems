# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(n):
            j = i + n
            answer += nums[i], nums[j]
        return answer