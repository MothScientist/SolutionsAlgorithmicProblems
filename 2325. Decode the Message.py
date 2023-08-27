class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_new = ""
        for i in key:
            if i != " " and i not in key_new:
                key_new += i
        alphabet = string.ascii_lowercase
        dictionary = {key_new[i]: alphabet[i] for i in range(26)}
        res = ""
        for i in message:
            if i == " ":
                res += i
            else:
                res += dictionary[i]
        return res