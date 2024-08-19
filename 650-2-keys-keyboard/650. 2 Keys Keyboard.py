class Solution:
    def minSteps(self, n: int) -> int:
        # Initialize the total steps required to 0
        steps = 0
        
        # Start with the smallest possible factor, which is 2
        factor = 2
        
        # Factorize the number n
        while n > 1:
            # While n is divisible by the current factor
            while n % factor == 0:
                # Add the factor to the steps (since we need this many "Paste" operations)
                steps += factor
                # Divide n by this factor to reduce it
                n //= factor
            # Move to the next possible factor
            factor += 1
        
        # Return the total number of steps required
        return steps
