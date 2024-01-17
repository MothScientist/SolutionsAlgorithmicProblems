class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        if '6' not in num:
            return int(num)
        i = num.find('6')
        return int(num[:i] + '9' + num[i+1:])