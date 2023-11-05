# 953. Verifying an Alien Dictionary

# disgusting task, so the solution is not mine

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char:i for i,char in enumerate(order)}
        def comp(w1, w2):
            for c1, c2 in zip(w1, w2):
                if d[c1] < d[c2]:
                    return True
                elif d[c2] < d[c1]:
                    return False
            return len(w1) <= len(w2)
        return all(comp(words[i],words[i+1]) for i in range(len(words)-1))