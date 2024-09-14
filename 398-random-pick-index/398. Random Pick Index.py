import random
from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        """
        Initialize object with the array nums

        :param nums: List[int] - The input array of integers
        """

        self.num_indices = defaultdict(list)
        for index, num in enumerate(nums):
            self.num_indices[num].append(index)
        

    def pick(self, target: int) -> int:

        indicies = self.num_indices[target]
        choosen_index = random.choice(indicies)
        return choosen_index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)