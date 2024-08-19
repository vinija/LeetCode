class Solution:
    def largestPalindrome(self, n: int) -> int:
        
        if n == 1:
            return 9
        
        upper_limit = 10**n-1
        lower_limit = 10**(n - 1)

        for first_half in range(upper_limit, lower_limit -1, -1):
            palindromic_number = int(str(first_half) + str(first_half)[::-1])

            for i in range(upper_limit, int(palindromic_number**0.5), -1):
                if palindromic_number % i == 0:
                    if lower_limit <= palindromic_number // i <= upper_limit:
                        return palindromic_number %1337
        
        return -1