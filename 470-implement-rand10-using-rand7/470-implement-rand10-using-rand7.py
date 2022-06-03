# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
		# Method 2: Mapping Rule 
        val1, val2 = rand7(), rand7()
		
		# val1 : {1,2,3,4,5,6,7} : Here, {6,7} are ignored to ensure equal probability for [1,5]
        while val1 > 5: val1 = rand7()
		
		# val2: {1,2,3,4,5,6,7} : Here, [1,3] correspond to [1,5] in the output and [4,6] correspond to [6,10]
		# {7} has been ignored to ensure equal probability distribution
        while val2 == 7: val2 = rand7()
		
        return val1 if val2 <= 3 else val1 + 5