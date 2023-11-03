class Solution:
    def countOrders(self, num_pairs: int) -> int:
        MOD = int(1e9 + 7)
        count = 1
        for current_pairs in range(1, num_pairs + 1):
            count = count * (2 * current_pairs - 1) * current_pairs % MOD
        return count