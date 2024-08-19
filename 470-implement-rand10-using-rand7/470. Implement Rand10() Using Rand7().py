# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number between 1 and 49 (since 7 * 7 = 49)
            num = (rand7() - 1) * 7 + rand7()
            
            # If the number is within the range 1 to 40, return a number between 1 and 10
            if num <= 40:
                return (num - 1) % 10 + 1