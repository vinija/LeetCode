class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if char in "+-*/" or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    stack.append(int(stack.pop() / current_number))  # Truncate towards zero
                
                operation = char
                current_number = 0
        
        return sum(stack)
