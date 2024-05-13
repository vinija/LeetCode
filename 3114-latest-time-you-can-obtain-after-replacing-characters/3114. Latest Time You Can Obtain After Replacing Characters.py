class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)  # Convert the string to a list for easy manipulation
        
        # Process hours tens place
        if s[0] == '?':
            if s[1] == '?' or int(s[1]) < 2:
                s[0] = '1'
            else:
                s[0] = '0'

        # Process hours units place
        if s[1] == '?':
            if s[0] == '1':
                s[1] = '1'  # Max hour for 12-hour format can be 11
            else:
                s[1] = '9'
        
        # Process minutes tens place
        if s[3] == '?':
            s[3] = '5'
        
        # Process minutes units place
        if s[4] == '?':
            s[4] = '9'

        # Convert list back to string and return
        return "".join(s)

# Example usage
sol = Solution()
print(sol.findLatestTime("1?:3?"))  # Output: "11:39"
print(sol.findLatestTime("?4:5?"))  # Output: "14:59"
print(sol.findLatestTime("??:??"))  # Output: "11:59"
