class Solution:
	def __init__(self, nums: List[int]):
		self.arr = nums  # Deep Copy, Can also use Shallow Copy concept!
		# self.arr = nums  # Shallow Copy would be something like this!

	def reset(self) -> List[int]:
		return self.arr

	def shuffle(self) -> List[int]:
		ans = self.arr[:]
		for i in range(len(ans)):
			swp_num = random.randrange(i, len(ans))  # Fisher-Yates Algorithm
			ans[i], ans[swp_num] = ans[swp_num], ans[i]
		return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()