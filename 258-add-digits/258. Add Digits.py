class Solution:
    def addDigits(self, num: int) -> int:
        # If num is 0, return 0
        if num == 0:
            return 0
        # If num is a multiple of 9, return 9 (unless num is 0, handled above)
        elif num % 9 == 0:
            return 9
        # Otherwise, return num modulo 9
        else:
            return num % 9

        