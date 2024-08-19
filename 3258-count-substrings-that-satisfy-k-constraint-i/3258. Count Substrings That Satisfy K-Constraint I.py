class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def count_valid_substrings(k: int) -> int:
            count = 0
            left = 0
            count_zeros = 0
            count_ones = 0
            
            for right in range(len(s)):
                if s[right] == '0':
                    count_zeros += 1
                elif s[right] == '1':
                    count_ones += 1
                
                # While the count of either '0's or '1's exceeds k, shrink the window
                while count_zeros > k and count_ones > k:
                    if s[left] == '0':
                        count_zeros -= 1
                    elif s[left] == '1':
                        count_ones -= 1
                    left += 1
                
                # Add the number of valid substrings ending at `right`
                count += (right - left + 1)
            
            return count

        return count_valid_substrings(k)

# Example usage:
sol = Solution()
print(sol.countKConstraintSubstrings("10101", 1))  # Expected output: 12
print(sol.countKConstraintSubstrings("1010101", 2))  # Expected output: 25
print(sol.countKConstraintSubstrings("11111", 1))  # Expected output: 15
