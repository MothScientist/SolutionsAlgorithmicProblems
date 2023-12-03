class Solution:
    def romanToInt(self, s: str) -> int:
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
