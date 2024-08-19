class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # Convert the input n from a string to an integer
        n = int(n)
        
        # The maximum possible length of the base-k representation with all 1's
        max_m = n.bit_length() - 1
        
        # Try all possible lengths from max_m down to 2
        for m in range(max_m, 1, -1):
            # Use binary search to find the smallest base k
            k = int(n ** (1 / m))
            
            # Calculate the sum of the geometric series for base k
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)
        
        # If no such k is found, return n-1 as the smallest base
        return str(n - 1)
