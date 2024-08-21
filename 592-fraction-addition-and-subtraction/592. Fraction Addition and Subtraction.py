from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Split the expression by '+' and '-' while keeping the sign with each fraction
        fractions = []
        i = 0
        if expression[0] == '-':
            fractions.append('-')
            i = 1
        
        while i < len(expression):
            start = i
            while i < len(expression) and expression[i] not in '+-':
                i += 1
            fractions.append(expression[start:i])
            if i < len(expression):
                fractions.append(expression[i])
                i += 1
        
        # Initialize the result as 0/1
        result = Fraction(0, 1)
        
        # Add/subtract each fraction in the list to the result
        i = 0
        while i < len(fractions):
            if fractions[i] == '-':
                result += Fraction(fractions[i+1]) * -1
                i += 2
            elif fractions[i] == '+':
                result += Fraction(fractions[i+1])
                i += 2
            else:
                result += Fraction(fractions[i])
                i += 1
        
        # Return the result as a string in the form of 'numerator/denominator'
        return f"{result.numerator}/{result.denominator}"
