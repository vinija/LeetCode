class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def wordToNumber(word: str) -> int:
            number = 0
            for char in word:
                number = number * 10 + (ord(char) - ord('a'))
            return number
        
        num1 = wordToNumber(firstWord)
        num2 = wordToNumber(secondWord)
        targetNum = wordToNumber(targetWord)

        return num1 + num2 == targetNum