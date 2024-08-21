from collections import Counter

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = Counter(s)
        num = count.get(letter, 0)  # Get the count of the letter, default to 0 if not found
        
        return (num * 100) // len(s)  # Multiply first, then integer division
