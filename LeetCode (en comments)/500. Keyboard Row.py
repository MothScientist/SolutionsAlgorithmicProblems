class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        res = []
        b = False

        for word in words:
            char = word[0].lower()
            if char in first_row:
                b = all([i.lower() in first_row for i in word])
            elif char in second_row:
                b = all([i.lower() in second_row for i in word])
            else:
                b = all([i.lower() in third_row for i in word])
            
            if b:
                res.append(word)

        return res