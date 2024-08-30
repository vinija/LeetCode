class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize the DP array and pointers
        ugly = [0] * n  # To store the first n ugly numbers
        ugly[0] = 1  # First ugly number is 1
        
        i2 = i3 = i5 = 0  # Pointers for multiples of 2, 3, and 5
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        
        for i in range(1, n):
            # Choose the smallest number among next multiples of 2, 3, and 5
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly[i] = next_ugly
            
            # Increment the pointer for which the multiple was chosen
            if next_ugly == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            
            if next_ugly == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            
            if next_ugly == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        
        return ugly[-1]

# Example usage:
solution = Solution()
print(solution.nthUglyNumber(10))  # Output: 12
