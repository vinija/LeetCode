class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def is_self_dividing(n: int) -> bool:
            original_n = n
            while n > 0:
                digit = n %10
                if digit == 0 or original_n % digit != 0:
                    return False
                
                n //= 10
            return True
        
        result = []

        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)

        return result