class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)  # Convert the string to a list for easy modification
        n = len(s)
        
        # Iterate over the first half of the string
        for i in range(n // 2):
            j = n - 1 - i  # Corresponding character from the other half
            # Replace both characters with the lexicographically smaller one
            if s[i] != s[j]:
                s[i] = s[j] = min(s[i], s[j])
        
        return ''.join(s)  # Join the list back into a string and return it
