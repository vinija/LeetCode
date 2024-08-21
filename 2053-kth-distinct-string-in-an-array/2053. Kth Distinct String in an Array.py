class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Create a dictionary to count the frequency of each string
        freq = {}
        for string in arr:
            freq[string] = freq.get(string, 0) + 1
        
        # Iterate through the array and count distinct strings
        count = 0
        for string in arr:
            if freq[string] == 1:  # Check if the string is distinct
                count += 1
                if count == k:  # Return the kth distinct string
                    return string
        
        return ""  # Return an empty string if there are fewer than k distinct strings
