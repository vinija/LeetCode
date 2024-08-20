class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define sets for each row of the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        def can_be_typed(word):
            lowercase_word = word.lower()
            if all(char in row1 for char in lowercase_word):
                return True
            if all(char in row2 for char in lowercase_word):
                return True
            if all(char in row3 for char in lowercase_word):
                return True
            return False
        
        # Filter and return words that can be typed using one row
        return [word for word in words if can_be_typed(word)]
        