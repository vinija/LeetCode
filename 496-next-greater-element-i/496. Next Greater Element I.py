class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        # Stack to keep track of the elements for which we haven't found the next greater element yet
        stack = []

        # Traverse the nums2 list from left to right
        for num in nums2:
            # As long as there's an element in the stack and the current number is greater than the element at the top of the stack
            while stack and num > stack[-1]:
                # The current number is the next greater element for the element at the top of the stack
                next_greater[stack.pop()] = num
            # Push the current number onto the stack
            stack.append(num)

        # For any remaining elements in the stack, there is no greater element to the right, so they map to -1
        while stack:
            next_greater[stack.pop()] = -1

        # Build the result list for nums1 based on the mapping in next_greater
        return [next_greater[num] for num in nums1]
