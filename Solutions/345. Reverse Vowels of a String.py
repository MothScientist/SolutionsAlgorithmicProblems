# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[right] in vowels and s[left] in vowels:

                s[right], s[left] = s[left], s[right]

                right -= 1
                left += 1

            else: 
                if s[right] not in vowels:
                    right -= 1

                if s[left] not in vowels:
                    left += 1

        return "".join([str(_) for _ in s])