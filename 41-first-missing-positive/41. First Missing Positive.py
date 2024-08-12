from typing import List

class Solution:

	def firstMissingPositive(self, nums: List[int]) -> int:
		#len of the nums
		n = len(nums)

		#Step 1: place all the numbers in their correct position
		for i in range(n):
			while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
				#Swap the current number to its correct position
				nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] -1]

		#Step 2: Check for first missing number and return
		for i in range(n):
			if nums[i] != i+1:
				return i + 1

		#If none found, then return n+1
		return n + 1

        