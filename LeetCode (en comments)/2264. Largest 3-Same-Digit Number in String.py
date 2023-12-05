class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num += " "
        p1 = -1
        counter = 0
        res = ""

        for i in num:
            if counter == 3:
                if p1 > res:
                    res = p1

            if i != p1:
                p1 = i
                counter = 1
            else:
                counter += 1

        if res:
            return f"{res}{res}{res}"
        else:
            return ""