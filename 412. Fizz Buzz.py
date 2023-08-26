class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    arr.append("FizzBuzz")
                else:
                    arr.append("Fizz")
            else:
                if i % 5 == 0:
                    arr.append("Buzz")
                else:
                    arr.append(f"{i}")
        return arr