class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count_vowels = 0
        for i in s[0:k]:
            if i in "aeiou":
                count_vowels+=1

        maximum_vowels = count_vowels
        
        for i in range(k, len(s)):
            j = i - k
            if s[i] in "aeiou":
                count_vowels+=1
            if s[j] in "aeiou":
                count_vowels-=1

            maximum_vowels = max(maximum_vowels,count_vowels)
            
        return maximum_vowels

