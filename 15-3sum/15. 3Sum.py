class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # We need to sort the list first!
        res = [] # Result list holding the triplets

        # len(nums)-2 is because we need at least 3 numbers to continue.
        for i in range(len(nums)-2): #1
        
            # Since the list is sorted, if nums[i] > 0, then all 
            # nums[j] with j > i are positive as well, and we cannot
            # have three positive numbers sum up to 0. Return immediately.
            if nums[i] > 0:
                break
                        
            # if i > 0 is because when i = 0, it doesn't need to check if it's a duplicate 
            # element since it doesn't even have a previous element to compare with.
            # and nums[i] == nums[i-1] to avoid duplicates. 
            if i > 0 and nums[i] == nums[i-1]: #2
                continue
                
            # Classic two pointer solution
            left = i + 1 #3
            right = len(nums) - 1 #4
            
            while left < right: 
                curr_sum = nums[i] + nums[left] + nums[right]
                                    
                if curr_sum > 0: # sum too large, move right ptr
                    right -= 1
                    
                elif curr_sum < 0: # sum too small, move left ptr
                    left += 1
                
                else:
                    res.append([nums[i], nums[left], nums[right]]) #5
                    
                    # the below 2 loops are to avoid duplicate triplets
                    # we need to skip elements that are identical to our
                    # current solution, otherwise we would have duplicated triples                    
                    while left < right and nums[left] == nums[left + 1]: #6
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:#7
                        right -= 1    #8
                
                    right -= 1 #9 
                    left += 1 #10
        
        return res