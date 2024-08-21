class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def is_valid(num1: int, num2: int, start: int) -> bool:
            while start < len(num):
                num3 = num1 + num2
                num3_str = str(num3)
                if not num.startswith(num3_str, start):
                    return False
                start += len(num3_str)
                num1, num2 = num2, num3
            return True
        
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1.startswith("0")) or (len(num2) > 1 and num2.startswith("0")):
                    continue
                if is_valid(int(num1), int(num2), j):
                    return True
        return False
