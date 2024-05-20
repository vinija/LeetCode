class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 1
        
        for i in range(2, n + 1):
            result = result * i * (2 * i - 1) % MOD
        
        return result
