class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        
        # Determine the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        
        # Use absolute values to avoid dealing with negative numbers during division
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Get the integer part
        integer_part = numerator // denominator
        res.append(str(integer_part))
        
        # Calculate initial remainder
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)
        
        res.append('.')
        
        # Dictionary to store remainders and their corresponding positions in the result string
        remainder_dict = {}
        # Fractional part
        while remainder != 0:
            # If this remainder has been seen before, it's the start of a cycle
            if remainder in remainder_dict:
                res.insert(remainder_dict[remainder], '(')
                res.append(')')
                break
            
            remainder_dict[remainder] = len(res)
            
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(res)

        