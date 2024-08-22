from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Extracting only the letters from the license plate and converting them to lowercase
        licensePlate = ''.join([char.lower() for char in licensePlate if char.isalpha()])
        
        # Counting the frequency of each character in the license plate
        license_count = Counter(licensePlate)
        
        # Initialize the result word as None and its length as a large number
        result = None
        min_length = float('inf')
        
        # Iterate over each word in the list
        for word in words:
            word_count = Counter(word)
            
            # Check if the word contains at least as many of each letter as required by the license plate
            if all(word_count[char] >= license_count[char] for char in license_count):
                # If the current word is shorter than the previous one found, update the result
                if len(word) < min_length:
                    min_length = len(word)
                    result = word
        
        return result
