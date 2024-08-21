class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Define a set of vowels
        vowels = set('aeiouAEIOU')
        
        # Find the middle of the string
        mid = len(s) // 2
        
        # Split the string into two halves
        first_half = s[:mid]
        second_half = s[mid:]
        
        # Count vowels in both halves
        count_first_half = sum(1 for char in first_half if char in vowels)
        count_second_half = sum(1 for char in second_half if char in vowels)
        
        # Return True if the counts are equal, otherwise False
        return count_first_half == count_second_half
