class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Use absolute values to avoid handling negative numbers
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        # Remainder
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(result)  # No fractional part
        
        result.append(".")
        
        # Map to store remainders and their corresponding positions in the result
        remainder_map = {}
        
        while remainder != 0:
            # If the remainder is already seen, we have a repeating part
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            
            # Store the position of this remainder
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            quotient = remainder // denominator
            result.append(str(quotient))
            remainder %= denominator
        
        return "".join(result)
