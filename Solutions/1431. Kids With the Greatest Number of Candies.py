# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = [False for x in range(len(candies))]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                answer[i] = True
        return answer