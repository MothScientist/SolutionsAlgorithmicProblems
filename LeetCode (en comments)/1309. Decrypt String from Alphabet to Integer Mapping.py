# 1309. Decrypt String from Alphabet to Integer Mapping
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res_str = ""
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == '#':
                res_str += chr(96+int(s[i:i+2]))
                i += 3
            else:
                res_str += chr(96+int(s[i]))
                i += 1
        return res_str