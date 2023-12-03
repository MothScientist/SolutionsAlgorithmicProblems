class Solution:
    def get_dict(self, s):
            dc = dict()
            for i in s:
                if i not in dc:
                    dc[i] = 1
                else:
                    dc[i] += 1
            return dc

    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_frequency = self.get_dict(chars)
        for word in words:
            word_dict = self.get_dict(word)
            flag = True
            for key, value in word_dict.items():
                if key not in char_frequency or value > char_frequency[key]:
                    flag = False
                if not flag:
                    break
            if flag:
                res += len(word)
        return res