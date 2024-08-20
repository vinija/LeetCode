class Solution:

    def __init__(self, m: int, n: int):
        
        self.m = m
        self.n = n
        self.total = m*n
        self.flipped = {}
        self.available = self.total

    def flip(self) -> List[int]:

        rand_index = random.randint(0, self.available -1)
        actual_index = self.flipped.get(rand_index, rand_index)
        self.flipped[rand_index] = self.flipped.get(self.available - 1, self.available -1)
        self.available -= 1

        return [actual_index // self.n, actual_index % self.n]
        

    def reset(self) -> None:

        self.flipped.clear()
        self.available = self.total
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()