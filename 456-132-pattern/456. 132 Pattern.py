class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Keep track of "3" pattern
        stack = []

        # Keep track of second element "2"
        second_element = float('-inf')

        # Iterate over the list in reverse order

        for i in range(len(nums) -1, -1, -1):
            if nums[i] < second_element:
                return True
            
            while stack and nums[i] > stack[-1]:
                second_element = stack.pop()
            
            stack.append(nums[i])

        return False
        