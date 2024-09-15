from typing import List
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Rearranges the characters of the string so that no two adjacent characters are the same.
        
        :param s: str - The input string to rearrange.
        :return: str - A valid rearranged string or an empty string if impossible.
        :raises ValueError: If the input string is empty.
        """
        if not s:
            raise ValueError("Input string 's' must not be empty.")
        
        # Step 1: Count the frequency of each character in the string
        counter = Counter(s)
        max_allowed = (len(s) + 1) // 2  # Maximum frequency allowed for any character
        
        # Step 2: Check if the rearrangement is possible
        for char, freq in counter.items():
            if freq > max_allowed:
                return ""  # Impossible to rearrange
        
        # Step 3: Initialize a max heap based on character frequencies
        # Python's heapq is a min heap, so we store negative frequencies
        max_heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(max_heap)
        
        # Variables to keep track of the previous character
        prev_freq, prev_char = 0, ''
        
        result = []  # List to store the rearranged characters
        
        # Step 4: Rearrange the characters
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            # Since we've used one instance of 'char', decrement its frequency
            freq += 1  # Increment because frequencies are negative
            
            # If the previous character still has remaining frequency, push it back into the heap
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            # Update previous character to the current one
            prev_freq, prev_char = freq, char
        
        # Step 5: Verify if the rearranged string is valid
        rearranged = ''.join(result)
        if len(rearranged) != len(s):
            return ""  # Rearrangement was not possible
        return rearranged
