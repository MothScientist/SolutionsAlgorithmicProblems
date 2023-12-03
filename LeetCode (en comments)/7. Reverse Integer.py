# 7. Reverse Integer

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

def reverse(self, x: int) -> int:
    if x > 0:
        answer = int(str(x)[::-1])
        if answer >= -(2**31) and answer <= (2**31 - 1):
            return answer 
        else: 
            return 0
    else:
        answer = int(str(-x)[::-1]) * -1
        if answer >= -(2**31) and answer <= (2**31 - 1):
            return answer 
        else: 
            return 0