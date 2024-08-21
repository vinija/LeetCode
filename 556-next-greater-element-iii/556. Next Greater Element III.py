class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i == -1:
            return -1
        
        # Step 2: Find the element just larger than nums[i] to swap with
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap elements at i and j
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the sequence after the position i
        nums = nums[:i + 1] + nums[i + 1:][::-1]
        
        result = int(''.join(nums))
        
        # Step 5: Check if the result fits within a 32-bit integer
        return result if result <= 2**31 - 1 else -1
