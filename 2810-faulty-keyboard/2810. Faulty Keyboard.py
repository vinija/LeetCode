class Solution:
    def finalString(self, s: str) -> str:
        result = []  # Initialize an empty list to store the characters

        # Iterate over each character in the string
        for char in s:
            if char == 'i':
                result.reverse()  # Reverse the current result if the character is 'i'
            else:
                result.append(char)  # Append the character to the result if it's not 'i'

        return ''.join(result)  # Join the list into a string and return it
