class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Create a dictionary to store the substitution table
        substitution_table = {}
        alphabet = 'a'
        
        # Build the substitution table
        for char in key:
            if char.isalpha() and char not in substitution_table:
                substitution_table[char] = alphabet
                alphabet = chr(ord(alphabet) + 1)
                if alphabet > 'z':  # If we've assigned all letters, stop
                    break
        
        # Decode the message using the substitution table
        decoded_message = []
        for char in message:
            if char == ' ':
                decoded_message.append(' ')
            else:
                decoded_message.append(substitution_table[char])
        
        return ''.join(decoded_message)
