class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: if the expression is a number, return it as the only result
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Divide the expression at every operator
        for i, char in enumerate(expression):
            if char in "+-*":
                # Solve the left and right sub-expressions recursively
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results from the left and right with the current operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
        
        return results
