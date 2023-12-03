class Solution:
    def numberOfWays(self, corridor: str) -> int:
        chairs = 0
        plants = 0
        res = 1
        count_of_chair = corridor.count("S")
        if count_of_chair % 2 != 0 or count_of_chair < 2:
            return 0
        for i in corridor:
            if i == "P":
                # add a plant counter if the number of chairs in the back is divisible by 2 and not equal to 0
                if chairs % 2 == 0 and chairs:
                    plants += 1
            else:
                chairs += 1
                if chairs % 2 == 1:  # reset the counter by crossing the odd chair
                    res *= plants + 1  # +1, since you can put a partition between the chairs if they are not in a pair
                    plants = 0
                
        return res % (10**9 + 7)