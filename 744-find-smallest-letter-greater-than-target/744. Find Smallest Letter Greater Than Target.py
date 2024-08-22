class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(letters)

        for let in letters:
            if let > target:
                return let
        return letters[0]