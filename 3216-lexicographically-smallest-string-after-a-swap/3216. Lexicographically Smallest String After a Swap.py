class Solution:
    def getSmallestString(self, s: str) -> str:
        # Convert the string to a list to perform in-place swaps
        s = list(s)
        
        # Traverse the string to find adjacent digits with the same parity
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i + 1]) % 2:  # Check if both have the same parity
                # Check if swapping will result in a smaller string
                if s[i] > s[i + 1]:
                    s[i], s[i + 1] = s[i + 1], s[i]  # Swap them
                    break  # Only one swap is allowed
        
        # Return the string after the swap
        return ''.join(s)

# Example usage:
sol = Solution()
print(sol.getSmallestString("45320"))  # Expected Output: "43520"
