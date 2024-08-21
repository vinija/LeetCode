class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # Split the sentence into words
        sorted_words = [''] * len(words)  # Create a list to store the sorted words
        
        # Place each word in its correct position based on the appended number
        for word in words:
            index = int(word[-1]) - 1  # Extract the index and convert it to 0-based
            sorted_words[index] = word[:-1]  # Remove the number and place the word
        
        return ' '.join(sorted_words)  # Join the sorted words to form the original sentence
