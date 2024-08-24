from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)  # Dictionary to count types of fruits in the current window
        left = 0  # Left pointer of the sliding window
        max_fruits = 0  # To store the maximum number of fruits we can collect
        
        # Iterate through the list of fruits with the right pointer
        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1  # Add the current fruit to the count
            
            # While there are more than 2 types of fruits in the window
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1  # Reduce the count of the fruit at the left pointer
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]  # Remove the fruit type if its count is 0
                left += 1  # Move the left pointer to the right
            
            # Update the maximum number of fruits we can collect
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
