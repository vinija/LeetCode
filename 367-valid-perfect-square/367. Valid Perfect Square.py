class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
